import socket
from _thread import *
import sys
from data import Data
import pickle

server = "192.168.0.24"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

currentPlayer = 0
all_data = [Data(0, currentPlayer), Data(0, currentPlayer)]

def threaded_client(conn, player):
    conn.send(pickle.dumps(all_data[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            all_data[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = all_data[0]
                else:
                    reply = all_data[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    all_data = [Data(0, currentPlayer), Data(0, currentPlayer)]



