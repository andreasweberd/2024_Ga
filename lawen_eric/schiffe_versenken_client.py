import socket

HOST = "192.168.168.133"  # The server's hostname or IP address
PORT = 1234  # The port used by the server

spielfeld = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1],
]

hits = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

def shoot(conn):
    x = input("X-Koordinate: ")
    y = input("Y-Koordinate: ")
    message = bytes("SHOTX"+str(x)+"Y"+str(y),'UTF-8')
    conn.sendall(message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"HELLO")
    print(f"Send HELLO")
    while True:
        data = s.recv(1024)
        if data == b"OK":
            print(f"OK received")
            shoot(s)
        elif data == b"MISS":
            print(f"MISS")
        elif data == b"DEAD":
            print(f"YOU WON")
        elif data == b"HIT":
            print(f"HIT")
            shoot(s)
        elif data == b"TILT":
                print(f"Schiff versenkt")
                shoot(s)
        elif b"SHOT" in data:
                x = int(data.decode()[data.decode().find('X') + 1 : data.decode().find('X') + 2 : 1])
                print('X = '+str(x))
                y = int(data.decode()[data.decode().find('Y') + 1 : data.decode().find('Y') + 2 : 1])
                print('Y = '+str(y))
                if spielfeld[x][y] == 1:
                    print("ENEMY HIT")
                    hits[x][y] = 1
                    if hits == spielfeld:
                        print("DEAD")
                        s.sendall(b"DEAD")
                    else:
                        s.sendall(b"HIT")
                elif spielfeld[x][y] == 0:
                    print("ENEMY MISS")
                    shoot(s)
        elif not data:
            break
        """ s.sendall(data) """