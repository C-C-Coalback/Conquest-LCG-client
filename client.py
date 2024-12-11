import socket
from threading import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8089))

def send():
    running = True
    try:
        while running:
            message = input("Message")
            client_socket.send(bytes(message, 'UTF-8'))
            if message == "QUIT":
                running = False
    except ConnectionAbortedError:
        print("Connection aborted")

def recv():
    running = True
    try:
        while running:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print("Server sent:", message)
    except ConnectionAbortedError:
        print("Connection aborted")


Thread(target=recv).start()
Thread(target=send).start()