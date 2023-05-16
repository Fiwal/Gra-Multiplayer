import pickle
import socket

from constants import *

class Network:
    def __init__(self):
        # Tworzenie gniazda sieciowego (socket) z rodzajem AF_INET (IPv4) i typem SOCK_STREAM (TCP)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER
        self.port = PORT
        self.addr = (self.server, self.port)
        self.player = self.connect()

    def get_player(self):
        return self.player

    # Ta funkcja łączy się z serwerem.
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(4096 * 4))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096 * 4))
        except socket.error as e:
            print(e)