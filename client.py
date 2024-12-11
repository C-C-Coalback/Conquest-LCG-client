import socket, sys
import Replace
from threading import *
import pygame

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8089))

def send():
    running = True
    pygame.init()
    bounds = (1200, 700)
    window = pygame.display.set_mode(bounds)
    pygame.display.set_caption("Conquest")
    imperial_image = pygame.image.load("ImperialAquila.jpg").convert()
    window.blit(imperial_image, (0, 0))
    font = pygame.font.Font(None, 32)
    color = pygame.Color("green")
    txt_surface = font.render("Press p to play", True, color)
    window.blit(txt_surface, (500, 300))
    txt_surface2 = font.render("Press d to build a deck", True, color)
    window.blit(txt_surface2, (500, 325))
    pygame.display.flip()
    try:
        while running:
            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    pygame.quit()
                    client_socket.close()
                    sys.exit()
                if x.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    message = str(x) + '#' + str(y)
                    client_socket.send(bytes(message, "UTF-8"))

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

user_input = input("g to connect to server, r to resize files")
if user_input == "g":
    Thread(target=recv).start()
    Thread(target=send).start()
elif user_input == "r":
    client_socket.close()
    Replace.resize_files()