package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"net"
	"os"
	"strings"
	"sync"
	"time"
)

const (
	HOST            = "10.8.0.8"
	PORT            = "1234"
	BOARD_SIZE      = 10
	SHIP_COUNT      = 5
	SHIP_LENGTH_MIN = 2
	SHIP_LENGTH_MAX = 7
)

var (
	targets  []string
	targetMu sync.Mutex
)

func init() {
	for e := 0; e < 10; e++ {
		for x := 0; x < 10; x++ {
			targets = append(targets, fmt.Sprintf("X%dY%d", x, e))
		}
	}
	rand.Seed(time.Now().UnixNano())
}

func printBoard(board [][]string) {
	fmt.Print("   ")
	for i := 0; i < BOARD_SIZE; i++ {
		fmt.Printf("%2d ", i)
	}
	fmt.Println()
	for y, row := range board {
		fmt.Printf("%2d ", y)
		for _, cell := range row {
			fmt.Printf("%s  ", cell)
		}
		fmt.Println()
	}
}

func createEmptyBoard() [][]string {
	board := make([][]string, BOARD_SIZE)
	for i := range board {
		board[i] = make([]string, BOARD_SIZE)
		for j := range board[i] {
			board[i][j] = "."
		}
	}
	return board
}

func placeShipsRandomly() ([][]string, [][4]interface{}) {
	board := createEmptyBoard()
	var ships [][4]interface{}
	attempts := 0
	for len(ships) < SHIP_COUNT && attempts < 1000 {
		length := rand.Intn(SHIP_LENGTH_MAX-SHIP_LENGTH_MIN+1) + SHIP_LENGTH_MIN
		orientation := "H"
		if rand.Intn(2) == 1 {
			orientation = "V"
		}
		var row, col int
		if orientation == "H" {
			row = rand.Intn(BOARD_SIZE)
			col = rand.Intn(BOARD_SIZE - length + 1)
		} else {
			row = rand.Intn(BOARD_SIZE - length + 1)
			col = rand.Intn(BOARD_SIZE)
		}
		if canPlaceShip(board, row, col, length, orientation) {
			placeShip(board, row, col, length, orientation)
			ships = append(ships, [4]interface{}{row, col, length, orientation})
		}
		attempts++
	}
	if len(ships) < SHIP_COUNT {
		fmt.Println("Warnung: Nicht alle Schiffe konnten platziert werden.")
	}
	return board, ships
}

func canPlaceShip(board [][]string, row, col, length int, orientation string) bool {
	for i := 0; i < length; i++ {
		var r, c int
		if orientation == "H" {
			r = row
			c = col + i
		} else {
			r = row + i
			c = col
		}
		if board[r][c] != "." {
			return false
		}
		for dr := -1; dr <= 1; dr++ {
			for dc := -1; dc <= 1; dc++ {
				rr := r + dr
				cc := c + dc
				if rr >= 0 && rr < BOARD_SIZE && cc >= 0 && cc < BOARD_SIZE {
					if board[rr][cc] == "S" {
						return false
					}
				}
			}
		}
	}
	return true
}

func placeShip(board [][]string, row, col, length int, orientation string) {
	for i := 0; i < length; i++ {
		var r, c int
		if orientation == "H" {
			r = row
			c = col + i
		} else {
			r = row + i
			c = col
		}
		board[r][c] = "S"
	}
}

func coordToStr(row, col int) string {
	return fmt.Sprintf("X%dY%d", col, row)
}

func strToCoord(s string) (int, int, bool) {
	s = strings.TrimSpace(s)
	x := strings.Index(s, "X")
	y := strings.Index(s, "Y")
	if x == -1 || y == -1 || y < x {
		return 0, 0, false
	}
	col := 0
	row := 0
	_, err1 := fmt.Sscanf(s[x+1:y], "%d", &col)
	_, err2 := fmt.Sscanf(s[y+1:], "%d", &row)
	if err1 != nil || err2 != nil {
		return 0, 0, false
	}
	if col < 0 || col > 9 || row < 0 || row > 9 {
		return 0, 0, false
	}
	return row, col, true
}

type BattleshipClient struct {
	conn        net.Conn
	ownBoard    [][]string
	enemyBoard  [][]string
	myTurn      bool
	running     bool
	ships       [][4]interface{}
}

func NewBattleshipClient(host, port string) *BattleshipClient {
	conn, err := net.Dial("tcp", host+":"+port)
	if err != nil {
		fmt.Println("Fehler beim Verbinden:", err)
		os.Exit(1)
	}
	ownBoard, ships := placeShipsRandomly()
	client := &BattleshipClient{
		conn:       conn,
		ownBoard:   ownBoard,
		enemyBoard: createEmptyBoard(),
		ships:      ships,
		running:    true,
		myTurn:     false,
	}
	client.send("HELLO")
	return client
}

func (bc *BattleshipClient) send(msg string) {
	bc.conn.Write([]byte(msg + "\n"))
}

func (bc *BattleshipClient) receiveLoop() {
	scanner := bufio.NewScanner(bc.conn)
	for bc.running {
		if !scanner.Scan() {
			fmt.Println("Verbindung getrennt.")
			bc.running = false
			break
		}
		line := scanner.Text()
		bc.handleMessage(strings.TrimSpace(line))
	}
}

func (bc *BattleshipClient) handleMessage(message string) {
	fmt.Println("Empfangen:", message)
	switch {
	case message == "HELLO":
		bc.send("OK")
		fmt.Println("Verbindung steht. Deine Schiffe:")
		printBoard(bc.ownBoard)
		bc.myTurn = true
		if bc.myTurn {
			fmt.Println("Du bist am Zug!")
			bc.makeMove()
		}
	case message == "OK":
		fmt.Println("Verbindung steht. Deine Schiffe sind platziert:")
		printBoard(bc.ownBoard)
		fmt.Println("Du beginnst. Wohin willst du schießen?")
		bc.myTurn = true
		bc.makeMove()
	case strings.HasPrefix(message, "SHOT"):
		coordStr := message[4:]
		r, c, ok := strToCoord(coordStr)
		result := ""
		if ok {
			result = bc.checkHit(r, c)
			fmt.Printf("Gegner schießt auf %s: %s\n", coordStr, result)
		} else {
			fmt.Printf("Ungültige Koordinate vom Gegner: %s\n", coordStr)
			result = "MISS"
		}
		bc.send(result)
		if result == "DEAD" {
			fmt.Println("Du hast verloren!")
			bc.running = false
		} else if result == "HIT" {
			bc.myTurn = false
		} else {
			bc.myTurn = true
			if bc.myTurn {
				bc.makeMove()
			}
		}
	case message == "HIT" || message == "MISS" || message == "TILT" || message == "DEAD":
		fmt.Printf("Antwort auf deinen Schuss: %s\n", message)
		if message == "DEAD" {
			fmt.Println("Du hast gewonnen!")
			bc.running = false
		}
		if message == "HIT" || message == "TILT" {
			bc.myTurn = true
			if bc.myTurn {
				bc.makeMove()
			}
		} else {
			bc.myTurn = false
			fmt.Println("Warte auf den Zug des Gegners...")
		}
	default:
		fmt.Printf("Unbekannte Nachricht: %s\n", message)
	}
}

func (bc *BattleshipClient) makeMove() {
	targetMu.Lock()
	if len(targets) == 0 {
		fmt.Println("Keine Ziele mehr übrig!")
		targetMu.Unlock()
		return
	}
	move := targets[0]
	targets = targets[1:]
	targetMu.Unlock()
	bc.send("SHOT" + move)
}

func (bc *BattleshipClient) checkHit(r, c int) string {
	if r < 0 || r >= BOARD_SIZE || c < 0 || c >= BOARD_SIZE {
		return "MISS"
	}
	if bc.ownBoard[r][c] == "S" {
		bc.ownBoard[r][c] = "X"
		alive := false
		for _, row := range bc.ownBoard {
			for _, cell := range row {
				if cell == "S" {
					alive = true
					break
				}
			}
		}
		if !alive {
			return "DEAD"
		}
		return "HIT"
	} else if bc.ownBoard[r][c] == "." {
		bc.ownBoard[r][c] = "O"
		return "MISS"
	}
	return "MISS"
}

func (bc *BattleshipClient) close() {
	bc.running = false
	bc.conn.Close()
}

func main() {
	client := NewBattleshipClient(HOST, PORT)
	go client.receiveLoop()
	for client.running {
		time.Sleep(100 * time.Millisecond)
	}
	client.close()
}
