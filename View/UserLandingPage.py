import pygame
import random
import os

from Model.Network import Network
from Model.Player import Player
from View.Button import Button
from View.Checkbox import Checkbox
from View.DropdownMenu import DropdownMenu
from View.LineEdit import LineEdit

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

GRID_WIDTH = 32
GRID_HEIGHT = 18

CELL_WIDTH = SCREEN_WIDTH/GRID_WIDTH
CELL_HEIGHT = SCREEN_HEIGHT/GRID_HEIGHT

fullscreen = True

# game window
def refreshWindow(fullscreen):
    if fullscreen:
        return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen = refreshWindow(fullscreen)

pygame.display.set_caption("SPECTRAVIA TCG SIM")
# Quando avro' un icona: pygame.display.set_icon("")
bg_image = pygame.image.load("Assets/background.jpg")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colors
TEXT_COL = (255,255,255)

# load buttons
multiplayer_img = pygame.image.load("Assets/Other/Buttons/multiplayer.png").convert_alpha()
deckEditor_img = pygame.image.load("Assets/Other/Buttons/deck_editor.png").convert_alpha()
settings_img = pygame.image.load("Assets/Other/Buttons/settings.png").convert_alpha()
back_img = pygame.image.load("Assets/Other/Buttons/back.png").convert_alpha()
quit_img = pygame.image.load("Assets/Other/Buttons/quit.png").convert_alpha()

multiplayer_btn = Button(CELL_WIDTH, 2*CELL_HEIGHT, multiplayer_img, 1)
deckEditor_btn = Button(CELL_WIDTH, 5*CELL_HEIGHT, deckEditor_img, 1)
settings_btn = Button(CELL_WIDTH, 8*CELL_HEIGHT, settings_img, 1)
back_btn = Button(CELL_WIDTH, 12*CELL_HEIGHT, back_img, 1)
quit_btn = Button(CELL_WIDTH, 14*CELL_HEIGHT, quit_img, 1)

# load lineEdit
nameEdit = LineEdit(CELL_WIDTH, 12*CELL_HEIGHT, 8*CELL_WIDTH, CELL_HEIGHT)

# load fullscreen Checkbox
fullscreenCheckbox = Checkbox(CELL_WIDTH,4*CELL_HEIGHT,30, "     Fullscreen")

# load resolution dropdown menu
resDropdownMenu = DropdownMenu(CELL_WIDTH, 4*CELL_HEIGHT, 30)

# load spectravia logo
game_logo = pygame.image.load("Assets/Other/spectravia_title.png")

clientNumber = 0

def randomizeCharacter():
    folder = "Assets/Other/Characters"
    fileNumber = len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
    r = random.randint(1, fileNumber)
    character_img = pygame.image.load("Assets/Other/Characters/character_" + str(r) + ".jpg")
    character_img = pygame.transform.scale(character_img, (10*CELL_WIDTH, 10*CELL_WIDTH))
    return character_img

character = randomizeCharacter()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def gameLoop():
    global screen, fullscreen
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
                
                screen.blit(game_logo, (20*CELL_WIDTH, 3*CELL_HEIGHT))
                screen.blit(character, (20*CELL_WIDTH, 4*CELL_HEIGHT))

                nameEdit.update()
                nameEdit.draw(screen)

                if quit_btn.draw(screen):
                    run = False

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
                draw_text("SpectraviaTCG, made by Lorenzo Zulli", font, TEXT_COL, CELL_WIDTH, 3*CELL_HEIGHT)

                fullscreenCheckbox.draw(screen)
                resDropdownMenu.draw(screen)

                fullscreenCheckbox.checked = fullscreen
                
                screen.blit(game_logo, (20*CELL_WIDTH, 3*CELL_HEIGHT))
                screen.blit(character, (20*CELL_WIDTH, 4*CELL_HEIGHT))
                
                if back_btn.draw(screen):
                    menuState = "main"
                
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            nameEdit.handle_event(event)
            fullscreenCheckbox.handle_event(event)

            if fullscreen != fullscreenCheckbox.checked:
                fullscreen = fullscreenCheckbox.checked
                screen = refreshWindow(fullscreen)

        pygame.display.flip() 