### -------------------------------------------- ###
import pygame
import random
import os

from src.controller.PdfManager import PdfManager
from src.model.Network import Network
from src.model.Player import Player
from src.model.Button import Button
from src.model.Checkbox import Checkbox
from src.model.DropdownMenu import DropdownMenu
from src.model.LineEdit import LineEdit
### -------------------------------------------- ###

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
def refreshWindow(fullscreen, SCREEN_WIDTH, SCREEN_HEIGHT):
    if fullscreen:
        return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen = refreshWindow(fullscreen, SCREEN_WIDTH, SCREEN_HEIGHT)

def loadAssets(CELL_WIDTH, CELL_HEIGHT):
    # Caption and game icon
    pygame.display.set_caption("SPECTRAVIA TCG SIM")
    # Quando avro' un icona: pygame.display.set_icon("")

    # BG image load and scale
    bg_image = pygame.image.load("assets/graphics/GUI/background.jpg")
    bg_image = pygame.transform.scale(bg_image, (32*CELL_WIDTH, 18*CELL_HEIGHT))

    # define fonts
    font = pygame.font.SysFont("arialblack", 40)

    # define colors
    TEXT_COL = (255,255,255)

    # load buttons
    multiplayer_img = pygame.image.load("assets/graphics/GUI/Buttons/multiplayer.png").convert_alpha()
    deckEditor_img = pygame.image.load("assets/graphics/GUI/Buttons/deck_editor.png").convert_alpha()
    settings_img = pygame.image.load("assets/graphics/GUI/Buttons/settings.png").convert_alpha()
    back_img = pygame.image.load("assets/graphics/GUI/Buttons/back.png").convert_alpha()
    quit_img = pygame.image.load("assets/graphics/GUI/Buttons/quit.png").convert_alpha()

    multiplayer_btn = Button(CELL_WIDTH, 2*CELL_HEIGHT, multiplayer_img, 1)
    deckEditor_btn = Button(CELL_WIDTH, 5*CELL_HEIGHT, deckEditor_img, 1)
    settings_btn = Button(CELL_WIDTH, 8*CELL_HEIGHT, settings_img, 1)
    back_btn = Button(CELL_WIDTH, 12*CELL_HEIGHT, back_img, 1)
    quit_btn = Button(CELL_WIDTH, 14*CELL_HEIGHT, quit_img, 1)

    downloadRules_btn = Button(CELL_WIDTH, 7*CELL_HEIGHT, multiplayer_img, 1)

    # load lineEdit
    nameEdit = LineEdit(CELL_WIDTH, 12*CELL_HEIGHT, 8*CELL_WIDTH, CELL_HEIGHT, int(CELL_HEIGHT.__round__(0)))

    # load fullscreen Checkbox
    fullscreenCheckbox = Checkbox(CELL_WIDTH,4*CELL_HEIGHT,30, "     Fullscreen")

    # Load resolution dropdown menu
    resDropdownMenu = DropdownMenu(CELL_WIDTH, 5*CELL_HEIGHT, 5*CELL_WIDTH, int(CELL_HEIGHT.__round__(0)), font, ["1360x768", "1920x1080"])

    # load spectravia logo
    game_title = pygame.image.load("assets/graphics/GUI/spectravia_title.png")

    # Return all assets in a dictionary
    return {
        "bg_image": bg_image,
        "font": font,
        "TEXT_COL": TEXT_COL,
        "multiplayer_btn": multiplayer_btn,
        "deckEditor_btn": deckEditor_btn,
        "settings_btn": settings_btn,
        "back_btn": back_btn,
        "quit_btn": quit_btn,
        "downloadRules_btn": downloadRules_btn,
        "nameEdit": nameEdit,
        "fullscreenCheckbox": fullscreenCheckbox,
        "resDropdownMenu": resDropdownMenu,
        "game_title": game_title
    }

clientNumber = 0

def randomizeCharacter(CELL_WIDTH, CELL_HEIGHT):
    folder = "assets/graphics/GUI/Characters"
    fileNumber = len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
    r = random.randint(1, fileNumber)
    character_img = pygame.image.load("assets/graphics/GUI/Characters/character_" + str(r) + ".jpg")
    character_img = pygame.transform.scale(character_img, (10*CELL_WIDTH, 10*CELL_WIDTH))
    return character_img

character = randomizeCharacter(CELL_WIDTH, CELL_HEIGHT)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def gameLoop():

    assets = loadAssets(CELL_WIDTH, CELL_HEIGHT)

    bg_image = assets["bg_image"]
    font = assets["font"]
    TEXT_COL = assets["TEXT_COL"]
    multiplayer_btn = assets["multiplayer_btn"]
    deckEditor_btn = assets["deckEditor_btn"]
    settings_btn = assets["settings_btn"]
    back_btn = assets["back_btn"]
    quit_btn = assets["quit_btn"]
    downloadRules_btn = assets["downloadRules_btn"]
    nameEdit = assets["nameEdit"]
    fullscreenCheckbox = assets["fullscreenCheckbox"]
    resDropdownMenu = assets["resDropdownMenu"]
    game_title = assets["game_title"]

    global screen, fullscreen, character
    prevOption = None
    run = True
    n = Network()
    clock = pygame.time.Clock()
    menuState = "main"

    new_w = info.current_w
    new_h = info.current_h
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
                
                screen.blit(game_title, (20*CELL_WIDTH, 3*CELL_HEIGHT))
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

                yourDeck = pygame.Rect((460, 20, 800, 300))
                cardsList = pygame.Rect((460, 340, 800, 300))
                
                pygame.draw.rect(screen, (255, 128, 55, 128), yourDeck)
                pygame.draw.rect(screen, (255, 128, 55, 128), cardsList)

                if back_btn.draw(screen):
                    menuState = "main"
            case "settings":
                draw_text("SpectraviaTCG, made by Lorenzo Zulli", font, TEXT_COL, CELL_WIDTH, 3*CELL_HEIGHT)
                screen.blit(game_title, (20*CELL_WIDTH, 3*CELL_HEIGHT))
                screen.blit(character, (20*CELL_WIDTH, 4*CELL_HEIGHT))
                
                fullscreenCheckbox.draw(screen)
                fullscreenCheckbox.checked = fullscreen

                resDropdownMenu.draw(screen)

                if downloadRules_btn.draw(screen):
                    pd = PdfManager()
                    pd.parsePdf("data/rules.pdf")

                if back_btn.draw(screen):
                    menuState = "main"
                
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            nameEdit.handle_event(event)
            fullscreenCheckbox.handle_event(event)
            resDropdownMenu.handle_event(event)

            if fullscreen != fullscreenCheckbox.checked:
                fullscreen = fullscreenCheckbox.checked
                screen = refreshWindow(fullscreen, SCREEN_WIDTH, SCREEN_HEIGHT)
                assets = loadAssets(SCREEN_WIDTH/GRID_WIDTH, SCREEN_HEIGHT/GRID_HEIGHT)

            if resDropdownMenu.selected_option != prevOption:
                if resDropdownMenu.selected_option == resDropdownMenu.options[0]:
                    fullscreen = False
                    new_w = 1360
                    new_h = 768
                elif resDropdownMenu.selected_option == resDropdownMenu.options[1]:
                    fullscreen = False
                    new_w = 1920
                    new_h = 1080

                screen = refreshWindow(fullscreen, new_w, new_h)
                assets = loadAssets(new_w/GRID_WIDTH, new_h/GRID_HEIGHT)
                character = randomizeCharacter (new_w/GRID_WIDTH, new_h/GRID_HEIGHT)
                bg_image = assets["bg_image"]
                font = assets["font"]
                TEXT_COL = assets["TEXT_COL"]
                multiplayer_btn = assets["multiplayer_btn"]
                deckEditor_btn = assets["deckEditor_btn"]
                settings_btn = assets["settings_btn"]
                back_btn = assets["back_btn"]
                quit_btn = assets["quit_btn"]
                downloadRules_btn = assets["downloadRules_btn"]
                nameEdit = assets["nameEdit"]
                fullscreenCheckbox = assets["fullscreenCheckbox"]
                resDropdownMenu = assets["resDropdownMenu"]
                game_title = assets["game_title"]
                    
                prevOption = resDropdownMenu.selected_option
        pygame.display.flip()