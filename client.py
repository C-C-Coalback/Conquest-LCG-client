import socket, sys

import PromptText
import Replace
from threading import *
import pygame
from Drawing import draw_all, draw_lobby
from PosFromClick import pos_from_click
from FindDeck import find_deck

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8089))
c = Condition()

string_from_server = ""
invitee = ""
phase = "Main Menu"


def send():
    global string_from_server
    global invitee
    global phase
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
    phase = "Main Menu"
    deck_loaded = False
    current_lobby = []
    try:
        while running:
            _ = pygame.time.wait(20)
            if phase == "Lobby":
                c.acquire()
                c.notify_all()
                holder_string = string_from_server
                holder_string = holder_string.split(sep="#")
                c.release()
                current_lobby = draw_lobby(window, holder_string, invitee)
            if phase == "Game":
                if not deck_loaded:
                    client_socket.send(bytes("SWITCH TO GAME MODE", "UTF-8"))
                    message = "LOAD DECK#" + find_deck(window)
                    client_socket.send(bytes(message, "UTF-8"))
                    deck_loaded = True
                c.acquire()
                c.notify_all()
                draw_all(window, string_from_server)
                c.release()
            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    pygame.quit()
                    client_socket.close()
                    sys.exit()
                if x.type == pygame.MOUSEBUTTONDOWN:
                    x_pos, y_pos = pygame.mouse.get_pos()
                    print(x_pos, y_pos)
                    message = pos_from_click(x_pos, y_pos, phase, invitee, current_lobby)
                    if message != "":
                        client_socket.send(bytes(message, "UTF-8"))
                if x.type == pygame.KEYDOWN:
                    if x.key == pygame.K_p and phase == "Main Menu":
                        name = PromptText.prompt_text(window, "Enter your display name")
                        name_to_send = "SET NAME#" + name
                        pygame.display.set_caption("Conquest - " + name)
                        pygame.display.flip()
                        client_socket.send(bytes(name_to_send, "UTF-8"))
                        keep_looping = True
                        while keep_looping:
                            client_socket.send(bytes("REQUEST OWN USERNAME", "UTF-8"))
                            pygame.time.wait(1000)
                            if string_from_server == name:
                                keep_looping = False
                        client_socket.send(bytes("REQUEST LOBBY", "UTF-8"))

                        phase = "Lobby"
                        """client_socket.send(bytes("BEGIN GAME", "UTF-8"))
                        message = "LOAD DECK#" + find_deck(window)
                        client_socket.send(bytes(message, "UTF-8"))
                        phase = "Game" """

    except ConnectionAbortedError:
        print("Connection aborted")


def recv():
    global string_from_server
    global invitee
    global phase
    running = True
    try:
        while running:
            message = client_socket.recv(200000).decode()
            if not message:
                break
            c.acquire()
            string_from_server = message
            if len(string_from_server) > 11:
                if string_from_server[:12] == "GAME INVITE#" and invitee == "":
                    print("got here")
                    invitee = string_from_server[12:]
            if string_from_server == "REQUEST WAS REFUSED":
                print("the request was refused")
                invitee = ""
            if string_from_server == "GAME IS STARTING":
                phase = "Game"
            c.notify_all()
            c.release()
            print("Server sent:", message)
    except ConnectionAbortedError:
        print("Connection aborted")


user_input = input("g to connect to server, r to resize files")
if user_input == "g":
    Thread(target=send).start()
    Thread(target=recv).start()
elif user_input == "r":
    client_socket.close()
    Replace.resize_files()
