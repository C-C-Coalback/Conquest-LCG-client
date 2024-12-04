import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8089))
client_socket.send(bytes("hello", 'UTF-8'))