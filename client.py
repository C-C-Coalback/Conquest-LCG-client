import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8089))

try:
    while True:
        message = input("Message")
        client_socket.send(bytes(message, 'UTF-8'))
except ConnectionAbortedError:
    print("Connection aborted")