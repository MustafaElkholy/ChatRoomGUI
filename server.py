from socket import *
from threading import Thread
from _thread import *
import threading

ConnectionID = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000

ConnectionID.bind((host, port))

ConnectionID.listen(5)

clients = [] 

def ConnectClients(connID, address):
    print(address[0] + " connected.")
    while True:
        message = connID.recv(2048)
        message = message.decode('utf=8')
        send_to_all(message, connID)

def send_to_all(message, connID):
    for client in clients:
        if client != connID:
            client.send(message.encode("utf=8"))

while True:
    session, address = ConnectionID.accept()
    clients.append(session)
    start_new_thread(ConnectClients, (session, address))

