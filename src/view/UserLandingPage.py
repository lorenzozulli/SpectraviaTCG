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

# Costanti globali
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_WIDTH = 32
GRID_HEIGHT = 18
FULLSCREEN_OPTIONS = ["1360x768", "1920x1080"]

class SpectraviaTCG:
    def __init__(self):
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.info = pygame.display.Info()
        
        # Impostazioni dello schermo
        self.fullscreen = True
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        self.cell_width = self.screen_width / GRID_WIDTH
        self.cell_height = self.screen_height / GRID_HEIGHT

        self.screen = self.refresh_window()
        self.assets = self.load_assets()
        self.character = self.randomize_character()

        # Stato del gioco
        self.menu_state = "main"
        self.prev_option = None

        # Oggetti di supporto
        self.clock = pygame.time.Clock()
        self.network = Network()

    def refresh_window(self):
        """Aggiorna la finestra in base alla modalità fullscreen."""
        flags = pygame.FULLSCREEN if self.fullscreen else 0
        return pygame.display.set_mode((self.screen_width, self.screen_height), flags)

    def load_assets(self):
        """Carica tutti gli asset e li organizza in un dizionario."""
        # Carica immagini
        bg_image = pygame.image.load("assets/graphics/GUI/background.jpg")
        bg_image = pygame.transform.scale(bg_image, (32 * self.cell_width, 18 * self.cell_height))
        
        game_title = pygame.image.load("assets/graphics/GUI/spectravia_title.png")
        
        # Font
        arial_black = pygame.font.SysFont("arialblack", 40)
        sora_typeface = pygame.font.Font("assets/fonts/Sora_Typeface/fonts_v2.1beta/Sora-Medium.ttf", 40)
        
        # Pulsanti
        button_img = pygame.image.load("assets/graphics/GUI/Buttons/button.png").convert_alpha()
        buttons = {
            "multiplayer": Button(self.cell_width, 2 * self.cell_height, button_img, "MULTIPLAYER", WHITE, sora_typeface, 72, 1),
            "deckEditor": Button(self.cell_width, 5 * self.cell_height, button_img, "DECK EDITOR", WHITE, sora_typeface, 72, 1),
            "settings": Button(self.cell_width, 8 * self.cell_height, button_img, "SETTINGS", WHITE, sora_typeface, 72, 1),
            "back": Button(self.cell_width, 12 * self.cell_height, button_img, "BACK", WHITE, sora_typeface, 72, 1),
            "quit": Button(self.cell_width, 14 * self.cell_height, button_img, "QUIT", WHITE, sora_typeface, 72, 1),
            "downloadRules": Button(self.cell_width, 7 * self.cell_height, button_img, "Download Rules", WHITE, sora_typeface, 72, 1)
        }
        
        # Componenti interattivi
        name_edit = LineEdit(self.cell_width, 12 * self.cell_height, 8 * self.cell_width, self.cell_height, int(self.cell_height))
        fullscreen_checkbox = Checkbox(self.cell_width, 4 * self.cell_height, 30, "     Fullscreen")
        res_dropdown_menu = DropdownMenu(self.cell_width, 5 * self.cell_height, 5 * self.cell_width, int(self.cell_height), arial_black, FULLSCREEN_OPTIONS)
        
        return {
            "bg_image": bg_image,
            "game_title": game_title,
            "font": arial_black,
            "sora_typeface": sora_typeface,
            "buttons": buttons,
            "name_edit": name_edit,
            "fullscreen_checkbox": fullscreen_checkbox,
            "res_dropdown_menu": res_dropdown_menu
        }

    def randomize_character(self):
        """Seleziona casualmente un personaggio."""
        folder = "assets/graphics/GUI/Characters"
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        character_img = pygame.image.load(os.path.join(folder, random.choice(files)))
        return pygame.transform.scale(character_img, (10 * self.cell_width, 10 * self.cell_height))

    def draw_text(self, text, font, color, x, y):
        """Disegna testo sullo schermo."""
        img = font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def handle_events(self):
        """Gestisce gli eventi globali."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.assets["name_edit"].handle_event(event)
            self.assets["fullscreen_checkbox"].handle_event(event)
            self.assets["res_dropdown_menu"].handle_event(event)

        # Cambia risoluzione
        self.update_resolution()

        return True

    def update_resolution(self):
        """Aggiorna la risoluzione in base alle scelte utente."""
        checkbox = self.assets["fullscreen_checkbox"]
        dropdown = self.assets["res_dropdown_menu"]
        
        if self.fullscreen != checkbox.checked:
            self.fullscreen = checkbox.checked
            self.screen = self.refresh_window()
        
        if dropdown.selected_option != self.prev_option:
            self.fullscreen = False
            self.screen_width, self.screen_height = map(int, dropdown.selected_option.split("x"))
            self.cell_width = self.screen_width / GRID_WIDTH
            self.cell_height = self.screen_height / GRID_HEIGHT
            self.screen = self.refresh_window()
            self.assets = self.load_assets()
            self.character = self.randomize_character()
            self.prev_option = dropdown.selected_option

    def draw_main_menu(self):
        """Disegna il menu principale."""
        self.screen.blit(self.assets["bg_image"], (0, 0))
        self.screen.blit(self.assets["game_title"], (20 * self.cell_width, 3 * self.cell_height))
        self.screen.blit(self.character, (20 * self.cell_width, 4 * self.cell_height))
        self.assets["name_edit"].update()
        self.assets["name_edit"].draw(self.screen)
        
        buttons = self.assets["buttons"]
        if buttons["multiplayer"].draw(self.screen):
            self.menu_state = "multiplayer"
        elif buttons["deckEditor"].draw(self.screen):
            self.menu_state = "deckEditor"
        elif buttons["settings"].draw(self.screen):
            self.menu_state = "settings"
        elif buttons["quit"].draw(self.screen):
            return False
        
        return True

    def draw_multiplayer_menu(self):
        """Disegna il menu multiplayer."""
        self.screen.blit(self.assets["bg_image"], (0, 0))
        self.draw_text("Multiplayer", self.assets["sora_typeface"], WHITE, self.cell_width, 3 * self.cell_height)

        buttons = self.assets["buttons"]
        if buttons["back"].draw(self.screen):
            self.menu_state = "main"

    def draw_deck_editor_menu(self):
        """Disegna il menu editor dei mazzi."""
        self.screen.blit(self.assets["bg_image"], (0, 0))
        self.draw_text("Deck Editor", self.assets["sora_typeface"], WHITE, self.cell_width, 3 * self.cell_height)

        # Disegna sezioni per le carte
        your_deck = pygame.Rect((460, 20, 800, 300))
        cards_list = pygame.Rect((460, 340, 800, 300))

        pygame.draw.rect(self.screen, (255, 128, 55, 128), your_deck)
        pygame.draw.rect(self.screen, (255, 128, 55, 128), cards_list)

        buttons = self.assets["buttons"]
        if buttons["back"].draw(self.screen):
            self.menu_state = "main"

    def draw_settings_menu(self):
        """Disegna il menu impostazioni."""
        self.screen.blit(self.assets["bg_image"], (0, 0))
        self.draw_text("Settings", self.assets["sora_typeface"], WHITE, self.cell_width, 3 * self.cell_height)
        self.screen.blit(self.assets["game_title"], (20 * self.cell_width, 3 * self.cell_height))
        self.screen.blit(self.character, (20 * self.cell_width, 4 * self.cell_height))

        # Disegna interattivi
        checkbox = self.assets["fullscreen_checkbox"]
        dropdown = self.assets["res_dropdown_menu"]
        checkbox.draw(self.screen)
        dropdown.draw(self.screen)

        # Disegna pulsanti
        buttons = self.assets["buttons"]
        if buttons["downloadRules"].draw(self.screen):
            rules = PdfManager()
            rules_text = rules.parsePdf("data/rules.pdf")
            self.draw_text(rules_text, self.assets["sora_typeface"], WHITE, self.cell_width, 6 * self.cell_height)

        if buttons["back"].draw(self.screen):
            self.menu_state = "main"

    def run(self):
        """Loop principale del gioco."""
        running = True
        while running:
            self.clock.tick(60)
            running = self.handle_events()

            match self.menu_state:
                case "main":
                    running = self.draw_main_menu()
                case "multiplayer":
                    self.draw_multiplayer_menu()
                case "deckEditor":
                    self.draw_deck_editor_menu()
                case "settings":
                    self.draw_settings_menu()

            pygame.display.flip()