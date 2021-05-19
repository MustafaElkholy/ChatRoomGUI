from socket import *
from tkinter import *
from _thread import *
import threading

ConnectionID = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000

window = Tk()
window.geometry('300x400')

Label(window, text='Enter message: ').grid(row=0)
message = Entry(window, width=30)
message.grid(row=0, column=1)


Label(window, text = 'Recieved messages').grid(row = 1, column = 0)
ReceivedMessage = Entry(window, width=30)
ReceivedMessage.grid(row = 1, column=1)


def recieved_thread(conn):
    while True:
        x = conn.recv(2048)
        ReceivedMessage.delete(0, len(ReceivedMessage.get()))
        ReceivedMessage.insert(0, x)
        

ConnectionID.connect((host, port))
start_new_thread(recieved_thread, (ConnectionID,))


def send():
    ConnectionID.send(message.get().encode("utf=8"))
    message.delete(0, len(message.get()))


btn = Button(window, text="send", width=10, command=send)
btn.grid(row=3, column=1)

window.mainloop()
