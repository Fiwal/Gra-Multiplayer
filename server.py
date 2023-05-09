import random
import socket
from _thread import *
import pickle
from player import Player
from constants import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
    print(s)
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, server Started")

players = []


def threaded_client(conn, player_number):

    conn.send(pickle.dumps(players[player_number]))
    reply = ""

    while True:

        try:
            data = pickle.loads(conn.recv(2048))
            players[player_number] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = players

                print(f"Received: {reply}")
                print(f"Sending: {reply}")

            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    try:
        players.pop(player_number)

    except:
        conn.close()

    conn.close()


currentPlayer = 0


while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}.")

    randColor = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    players.append(Player(0, 60 * currentPlayer, 50, 50, randColor))

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
