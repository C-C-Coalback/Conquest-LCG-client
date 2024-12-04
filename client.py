import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8089))
client_socket.send(bytes("1#T#1#-2#5", 'UTF-8'))
msg = client_socket.recv(1024)
while msg:
    print("Received:" + msg.decode())
    msg = client_socket.recv(1024)