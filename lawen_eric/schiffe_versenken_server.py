import socket

HOST = ""  # Standard loopback interface address (localhost)
PORT = 1234  # Port to listen on (non-privileged ports are > 1023)

""" HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3000  # The port used by the server """

spielfeld = [
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
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
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data == b"HELLO":
                print(f"HELLO received")
                conn.sendall(b"OK")
            elif data == b"DEAD":
                print(f"YOU WON")
            elif data == b"TILT":
                print(f"Schiff versenkt")
                shoot(conn)
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
                        conn.sendall(b"DEAD")
                    else:
                        conn.sendall(b"HIT")
                elif spielfeld[x][y] == 0:
                    print("ENEMY MISS")
                    shoot(conn)
            elif data == b"MISS":
                print(f"MISS")
            elif data == b"HIT":
                print(f"HIT")
                shoot(conn)
            elif not data:
                break
            """ conn.sendall(data) """