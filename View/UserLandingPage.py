import pygame
import random

from Model.Network import Network
from View.Button import Button
from View.LineEdit import LineEdit

pygame.init()

SCREEN_WIDTH = 1360
SCREEN_HEIGHT = 768

# game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SPECTRAVIA TCG SIM")
# Quando avro' un icona pygame.display.set_icon("")
bg_image = pygame.image.load("Assets/background.jpg")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# game variables
menuState = "main"

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colors
TEXT_COL = (255,255,255)

# load button images
multiplayer_img = pygame.image.load("Assets/Other/multiplayer.png").convert_alpha()
deckEditor_img = pygame.image.load("Assets/Other/deck_editor.png").convert_alpha()
settings_img = pygame.image.load("Assets/Other/settings.png").convert_alpha()

multiplayer_btn = Button(128, 128, multiplayer_img, 1)
deckEditor_btn = Button(128, 234, deckEditor_img, 1)
settings_btn = Button(128, 340, settings_img, 1)

# load lineEdit
nameEdit = LineEdit(128, 550, 396, 40)

# load spectravia logo
game_logo = pygame.image.load("Assets/Other/spectravia_text.png")

clientNumber = 0

def randomizeCharacter():
    r = random.randint(1, 3)
    character_img = pygame.image.load("Assets/Other/character_" + str(r) + ".jpg")
    character_img = pygame.transform.scale(character_img, (500, 500))
    return character_img

character = randomizeCharacter()

def redrawWindow(menuState):
    screen.fill((0,0,0))
    screen.blit(bg_image, (0,0))

    if multiplayer_btn.draw(screen):
        menuState = "multiplayer"
    elif deckEditor_btn.draw(screen):
        menuState = "deckEditor"
    elif settings_btn.draw(screen):
        menuState = "settings"

    match menuState:
        case "main":
            multiplayer_btn.draw(screen)
            deckEditor_btn.draw(screen)
            settings_btn.draw(screen)

            screen.blit(game_logo, (800, 128))
            screen.blit(character, (800, 268))

            nameEdit.update()
            nameEdit.draw(screen)
            
        case "multiplayer":
            pass
        case "deckEditor":
            pass
        case "settings":
            pass

    pygame.display.update()

def gameLoop():
    # game loop
    run = True
    n = Network()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            nameEdit.handle_event(event)
        redrawWindow(menuState)

                
