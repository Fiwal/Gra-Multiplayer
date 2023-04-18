import socket
from _thread import *


def read_pos(text):
    text = text.split(",")
    return int(text[0]), int(text[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


server = "192.168.1.85"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, server Started")

positions = [(0, 0), (100, 100)]

def threaded_client(conn, playerNum):
    conn.send(str.encode(make_pos(positions[playerNum])))
    print(str.encode(make_pos(positions[playerNum])))
    reply = ""
    while True:

        try:
            data = read_pos(conn.recv(2048).decode())
            positions[playerNum] = data

            if not data:
                print("Disconnected")
                break
            else:
                if playerNum == 1:
                    reply = positions[0]
                else:
                    reply = positions[1]

                print(f"Received: {reply}")
                print(f"Sending: {reply}")

            conn.sendall(str.encode(make_pos(reply)))

        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}.")

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
