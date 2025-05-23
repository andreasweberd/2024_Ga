import socket
import threading
import random
import time

HOST = '10.8.0.8'
PORT = 1234

BOARD_SIZE = 10
SHIP_COUNT = 5
SHIP_LENGTH_MIN = 2
SHIP_LENGTH_MAX = 7

LETTERS = "ABCDEFGHIJ"

targets = []

b = "ABCDEFGHIJ"

for e in range(0, 10):
    for x in range(0, 10):
        targets.append("X" + str(x) + "Y" + str(e))

def print_board(board):
    print("   " + " ".join(f"{i+1:2}" for i in range(BOARD_SIZE)))
    for y, row in enumerate(board):
        print(f"{y+1:2} " + " ".join(row))

def create_empty_board():
    return [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def place_ships_randomly():
    board = create_empty_board()
    ships = []
    attempts = 0

    while len(ships) < SHIP_COUNT and attempts < 1000:
        length = random.randint(SHIP_LENGTH_MIN, SHIP_LENGTH_MAX)
        orientation = random.choice(["H", "V"])
        if orientation == "H":
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - length)
            if can_place_ship(board, row, col, length, orientation):
                place_ship(board, row, col, length, orientation)
                ships.append((row, col, length, orientation))
        else:
            row = random.randint(0, BOARD_SIZE - length)
            col = random.randint(0, BOARD_SIZE - 1)
            if can_place_ship(board, row, col, length, orientation):
                place_ship(board, row, col, length, orientation)
                ships.append((row, col, length, orientation))
        attempts += 1

    if len(ships) < SHIP_COUNT:
        print("Warnung: Nicht alle Schiffe konnten platziert werden.")
    return board, ships

def can_place_ship(board, row, col, length, orientation):
    for i in range(length):
        r = row + i if orientation == "V" else row
        c = col + i if orientation == "H" else col
        if board[r][c] != ".":
            return False
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < BOARD_SIZE and 0 <= cc < BOARD_SIZE:
                    if board[rr][cc] == "S":
                        return False
    return True

def place_ship(board, row, col, length, orientation):
    for i in range(length):
        r = row + i if orientation == "V" else row
        c = col + i if orientation == "H" else col
        board[r][c] = "S"

def coord_to_str(row, col):
    return f"X{col+1}Y{row+1}"

def str_to_coord(s):
    try:
        x = int(s.split("X")[1].split("Y")[0]) - 1
        y = int(s.split("Y")[1]) - 1
        return y, x
    except:
        return None

class BattleshipClient:

    global targets

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.running = True
        self.own_board, self.ships = place_ships_randomly()
        self.enemy_board = create_empty_board()
        self.my_turn = False

        self.send("HELLO")

    def send(self, msg):
        self.sock.sendall((msg + "\n").encode())

    def receive_loop(self):
        while self.running:
            try:
                data = self.sock.recv(1024)
                if not data:
                    print("Verbindung getrennt.")
                    self.running = False
                    break
                messages = data.decode().strip().split("\n")
                for msg in messages:
                    self.handle_message(msg.strip())
            except Exception as e:
                print("Error: " + str(data))
                print("Fehler beim Empfang:", e)
                self.running = False
                break

    def handle_message(self, message):
        print(f"Empfangen: {message}")

        if message == "HELLO":
            self.send("OK")
            print("Verbindung steht. Deine Schiffe:")
            print_board(self.own_board)
            self.my_turn = True
            if self.my_turn:
                print("Du bist am Zug!")
                self.make_move()

        elif message == "OK":
            print("Verbindung steht. Deine Schiffe sind platziert:")
            print_board(self.own_board)
            print("Du beginnst. Wohin willst du schießen?")
            self.my_turn = True
            self.make_move()

        elif message.startswith("SHOT"):
            coord_str = message[4:]
            r, c = str_to_coord(coord_str)
            result = self.check_hit(r, c)
            print(f"Gegner schießt auf {coord_str}: {result}")
            self.send(result)

            if result == "DEAD":
                print("Du hast verloren!")
                self.running = False
            elif result == "HIT":
                self.my_turn = False
            else:
                self.my_turn = True
                if self.my_turn:
                    self.make_move()

        elif message in {"HIT", "MISS", "TILT", "DEAD"}:
            print(f"Antwort auf deinen Schuss: {message}")
            if message == "DEAD":
                print("Du hast gewonnen!")
                self.running = False
            if message in {"HIT", "TILT"}:
                self.my_turn = True
                if self.my_turn:
                    self.make_move()
            else:
                self.my_turn = False
                print("Warte auf den Zug des Gegners...")

        else:
            print(f"Unbekannte Nachricht: {message}")

    def close(self):
        self.running = False
        self.sock.close()

    def make_move(self):
        while True:
            #move = input("Wohin möchtest du schießen? (z. B. A5): ").strip().upper()
            move = targets[0]
            targets.pop(0)
            # if len(move) < 2 or not move[0].isalpha() or not move[1:].isdigit():
            #     print("Ungültiges Format. Bitte A1 bis J10 eingeben.")
            #     continue

            # row_char = move[0]
            # col_str = move[1:]

            # if row_char not in LETTERS:
            #     print("Ungültiger Buchstabe. Erlaubt sind A–J.")
            #     continue

            # try:
            #     col = int(col_str)
            #     if not 1 <= col <= 10:
            #         raise ValueError
            # except ValueError:
            #     print("Ungültige Zahl. Erlaubt sind 1–10.")
            #     continue

            # row = LETTERS.index(row_char)
            # col_index = col - 1

            # # Verhindere doppelte Schüsse
            # if self.enemy_board[row][col_index] != ".":
            #     print("Du hast dort bereits geschossen. Bitte wähle eine andere Koordinate.")
            #     continue

            # self.enemy_board[row][col_index] = "?"  # Als Schuss markiert
            # coord_str = coord_to_str(row, col_index)
            # print(f"Du schießt auf {move} → {coord_str}")
            self.send(f"SHOT{move}")
            break

    def check_hit(self, r, c):
        if self.own_board[r][c] == "S":
            self.own_board[r][c] = "X"
            if not any("S" in row for row in self.own_board):
                return "DEAD"
            return "HIT"
        elif self.own_board[r][c] == ".":
            self.own_board[r][c] = "O"
            return "MISS"
        else:
            return "MISS"


def main():
    client = BattleshipClient(HOST, PORT)
    threading.Thread(target=client.receive_loop, daemon=True).start()

    try:
        while client.running:
            pass
    except KeyboardInterrupt:
        print("Beende...")
    finally:
        client.close()

if __name__ == "__main__":
    main()
