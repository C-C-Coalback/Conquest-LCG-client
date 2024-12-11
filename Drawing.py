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

def draw_all(game_screen):
    imperial_image = pygame.image.load("ImperialAquila.jpg").convert()
    game_screen.blit(imperial_image, (0, 0))
    draw_mat(game_screen)
    draw_both_pass_button(game_screen)
    draw_both_action_button(game_screen)
    draw_resource_icon_both(game_screen)
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

