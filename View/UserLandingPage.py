import pygame
from Model.Network import Network
from View.Button import Button

pygame.init()

SCREEN_WIDTH = 1360
SCREEN_HEIGHT = 768

# game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Client")
# Quando avro' un icona pygame.display.set_icon("")
bg_image = pygame.image.load("Assets/background.jpg")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# game variables

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

clientNumber = 0

def redrawWindow():
    screen.fill((0,0,0))
    screen.blit(bg_image, (0,0))
    multiplayer_btn.draw(screen)
    deckEditor_btn.draw(screen)
    settings_btn.draw(screen)
    
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
        redrawWindow()

                
