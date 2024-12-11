import pygame
import sys

def draw_mat(game_screen):
    playmat = pygame.image.load("Playmat.png").convert()
    game_screen.blit(playmat, (0, 100))

def draw_action_button_player_one(game_screen):
    font = pygame.font.Font(None, 32)
    color = pygame.Color("blue")
    text = "Action"
    action_button = pygame.Rect(1100, 650, 100, 50)
    txt_surface = font.render(text, True, color)
    game_screen.blit(txt_surface, (action_button.x + 5, action_button.y + 5))
    pygame.draw.rect(game_screen, color, action_button, 2)

def draw_action_button_player_two(game_screen):
    font = pygame.font.Font(None, 32)
    color = pygame.Color("blue")
    text = "Action"
    action_button = pygame.Rect(0, 50, 100, 50)
    txt_surface = font.render(text, True, color)
    game_screen.blit(txt_surface, (action_button.x + 5, action_button.y + 5))
    pygame.draw.rect(game_screen, color, action_button, 2)

def draw_pass_button_player_one(game_screen):
    font = pygame.font.Font(None, 32)
    color = pygame.Color("red")
    text = "Pass"
    pass_button = pygame.Rect(1100, 600, 100, 50)
    txt_surface = font.render(text, True, color)
    game_screen.blit(txt_surface, (pass_button.x + 5, pass_button.y + 5))
    pygame.draw.rect(game_screen, color, pass_button, 2)

def draw_pass_button_player_two(game_screen):
    font = pygame.font.Font(None, 32)
    color = pygame.Color("red")
    text = "Pass"
    pass_button = pygame.Rect(0, 0, 100, 50)
    txt_surface = font.render(text, True, color)
    game_screen.blit(txt_surface, (pass_button.x + 5, pass_button.y + 5))
    pygame.draw.rect(game_screen, color, pass_button, 2)

def draw_both_pass_button(game_screen):
    draw_pass_button_player_one(game_screen)
    draw_pass_button_player_two(game_screen)

def draw_both_action_button(game_screen):
    draw_action_button_player_one(game_screen)
    draw_action_button_player_two(game_screen)

def draw_resource_icon_both(game_screen):
    icon = pygame.image.load("Netrunner_credit.png").convert()
    game_screen.blit(icon, (1000, 600))
    game_screen.blit(icon, (125, 50))

def draw_resources_both(game_screen, amount1, amount2):
    font = pygame.font.Font(None, 32)
    color = pygame.Color("green")
    txt_surface_one = font.render(amount1, True, color)
    game_screen.blit(txt_surface_one, (1019, 615))
    txt_surface_two = font.render(amount2, True, color)
    game_screen.blit(txt_surface_two, (144, 65))

def draw_planets_in_play(game_screen, planet_names_string, planets_in_play_string):
    x_c = 60
    y_c = 320
    planets = planet_names_string.split(sep="/")
    planets_in_play = planets_in_play_string.split(sep="/")
    for i in range(len(planets)):
        if planets_in_play[i] == "True":
            planet_name = planets[i]
            for letter in planet_name:
                if letter == " ":
                    planet_name= planet_name.replace(letter, "_")
            planet_image_name = "ResizedImages/" + planet_name + ".jpg"
            planet_image = pygame.image.load(planet_image_name).convert()
            game_screen.blit(planet_image, (x_c, y_c))
        x_c += 165

def draw_hands(game_screen, hand_p_one, hand_p_two):
    card_names_one = hand_p_one.split(sep="/")
    card_names_two = hand_p_two.split(sep="/")
    x_c = 300
    y_c = 595
    increment = 80
    for i in range(len(card_names_one)):
        card_image_name = "ResizedImages/" + card_names_one[i] + ".jpg"
        for letter in card_image_name:
            if letter == " ":
                card_image_name = card_image_name.replace(letter, "_")
        card_image = pygame.image.load(card_image_name).convert()
        game_screen.blit(card_image, (x_c, y_c))
        x_c += increment
    x_c = 200
    y_c = 25
    for i in range(len(card_names_two)):
        card_image_name = "ResizedImages/" + card_names_two[i] + ".jpg"
        for letter in card_image_name:
            if letter == " ":
                card_image_name = card_image_name.replace(letter, "_")
        card_image = pygame.image.load(card_image_name).convert()
        game_screen.blit(card_image, (x_c, y_c))
        x_c += increment

def draw_headquarters(game_screen, hq_p_one, hq_p_two):
    hq_bundles_1 = hq_p_one.split(sep="/")
    hq_bundles_2 = hq_p_two.split(sep="/")
    x_c = 300
    y_c = 500
    increment = 80
    for i in range(len(hq_bundles_1)):
        card_image_name = ""
        pos = 0
        while hq_bundles_1[i][pos] != "(":
            card_image_name = card_image_name + hq_bundles_1[i][pos]
            pos += 1
        card_image_name = "ResizedImages/" + card_image_name + ".jpg"
        for letter in card_image_name:
            if letter == " ":
                card_image_name = card_image_name.replace(letter, "_")
        card_image = pygame.image.load(card_image_name).convert()
        game_screen.blit(card_image, (x_c, y_c))
        x_c += increment
    x_c = 300
    y_c = 125
    for i in range(len(hq_bundles_2)):
        card_image_name = ""
        pos = 0
        while hq_bundles_2[i][pos] != "(":
            card_image_name = card_image_name + hq_bundles_2[i][pos]
            pos += 1
        card_image_name = "ResizedImages/" + card_image_name + ".jpg"
        for letter in card_image_name:
            if letter == " ":
                card_image_name = card_image_name.replace(letter, "_")
        card_image = pygame.image.load(card_image_name).convert()
        game_screen.blit(card_image, (x_c, y_c))
        x_c += increment

def draw_all(game_screen, string_from_server):
    imperial_image = pygame.image.load("ImperialAquila.jpg").convert()
    game_screen.blit(imperial_image, (0, 0))
    draw_mat(game_screen)
    draw_both_pass_button(game_screen)
    draw_both_action_button(game_screen)
    draw_resource_icon_both(game_screen)
    split_string = string_from_server.split(sep="#")
    if len(split_string) > 2:
        draw_resources_both(game_screen, split_string[1], split_string[2])
        draw_planets_in_play(game_screen, split_string[3], split_string[4])
        draw_hands(game_screen, split_string[5], split_string[6])
        draw_headquarters(game_screen, split_string[7], split_string[8])
    pygame.display.flip()

def draw_current_deck(game_screen,  current_deck):
    for letter in current_deck:
        if letter == " ":
            current_deck = current_deck.replace(letter, "_")
    image_names = current_deck.split("#")
    x = 100
    y = 100
    x_inc = 100
    y_inc = 100
    imperial_image = pygame.image.load("ImperialAquila.jpg").convert()
    game_screen.blit(imperial_image, (0, 0))
    card_image_name = "ResizedImages/LargerResizedImages/" + image_names[1] + ".jpg"
    card_image = pygame.image.load(card_image_name).convert()
    game_screen.blit(card_image, (x, y))
    x = x + x_inc * 2
    for i in range(2, 10):
        card_image_name = "ResizedImages/LargerResizedImages/" + image_names[i] + ".jpg"
        card_image = pygame.image.load(card_image_name).convert()
        game_screen.blit(card_image, (x, y))
        x += x_inc
    y += y_inc
    x = 100
    for i in range(10, len(image_names)):
        card_image_name = "ResizedImages/LargerResizedImages/" + image_names[i] + ".jpg"
        card_image = pygame.image.load(card_image_name).convert()
        game_screen.blit(card_image, (x, y))
        x += x_inc
        if x > 1000:
            x = 100
            y += y_inc
    pygame.display.flip()
    status = True
    while status:
        _ = pygame.time.wait(17)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = False

