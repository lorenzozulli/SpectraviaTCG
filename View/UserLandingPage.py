import pygame
import random
import os

from Model.Network import Network
from View.Button import Button
from View.LineEdit import LineEdit

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SPECTRAVIA TCG SIM")
# Quando avro' un icona: pygame.display.set_icon("")
bg_image = pygame.image.load("Assets/background.jpg")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colors
TEXT_COL = (255,255,255)

# load buttons
multiplayer_img = pygame.image.load("Assets/Other/multiplayer.png").convert_alpha()
deckEditor_img = pygame.image.load("Assets/Other/deck_editor.png").convert_alpha()
settings_img = pygame.image.load("Assets/Other/settings.png").convert_alpha()
back_img = pygame.image.load("Assets/Other/back.png").convert_alpha()

multiplayer_btn = Button(100, 128, multiplayer_img, 1)
deckEditor_btn = Button(100, 234, deckEditor_img, 1)
settings_btn = Button(100, 340, settings_img, 1)
back_btn = Button(100, 550, back_img, 1)

# load lineEdit
nameEdit = LineEdit(100, 550, 396, 40)

# load spectravia logo
game_logo = pygame.image.load("Assets/Other/spectravia_text.png")

clientNumber = 0

def randomizeCharacter():
    folder = "Assets/Other/Characters"
    fileNumber = len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
    r = random.randint(1, fileNumber)
    character_img = pygame.image.load("Assets/Other/Characters/character_" + str(r) + ".jpg")
    character_img = pygame.transform.scale(character_img, (400, 400))
    return character_img

character = randomizeCharacter()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def gameLoop():
    run = True
    n = Network()
    clock = pygame.time.Clock()
    menuState = "main"
    while run:
        clock.tick(60)

        screen.fill((0,0,0))
        screen.blit(bg_image, (0,0))

        match menuState:
            case "main":
                if multiplayer_btn.draw(screen):
                    menuState = "multiplayer"
                elif deckEditor_btn.draw(screen):
                    menuState = "deckEditor"
                elif settings_btn.draw(screen):
                    menuState = "settings"
                
                screen.blit(game_logo, (800, 128))
                screen.blit(character, (800, 268))

                nameEdit.update()
                nameEdit.draw(screen)
            case "multiplayer":
                draw_text("multiplayer", font, TEXT_COL, 160, 250)

                if back_btn.draw(screen):
                    menuState = "main"
            case "deckEditor":
                draw_text("deck editor", font, TEXT_COL, 160, 250)

                rect1 = pygame.Rect((460, 20, 800, 300))
                rect2 = pygame.Rect((460, 340, 800, 300))
                
                pygame.draw.rect(screen, (255, 128, 55, 128), rect1)

                pygame.draw.rect(screen, (255, 128, 55, 128), rect2)

                if back_btn.draw(screen):
                    menuState = "main"
            case "settings":
                draw_text("SpectraviaTCG, made by Lorenzo Zulli", font, TEXT_COL, 160, 250)

                screen.blit(game_logo, (800, 128))
                screen.blit(character, (800, 268))
                
                if back_btn.draw(screen):
                    menuState = "main"
                
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            nameEdit.handle_event(event)
        pygame.display.update() 
                
