### -------------------------------------------- ###
import pygame

from src.model.Player import Player
### -------------------------------------------- ###

class LineEdit(object):
    def __init__(self, x, y, width, height, font_size=30, text_color=(0, 0, 0), bg_color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = Player.randomizeName()
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.active = False
        self.cursor_visible = True
        self.cursor_counter = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Sinistro del mouse
                # Attiva/Disattiva l'input in base al click del mouse
                if self.rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            # Gestione input tastiera
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.saved_text = self.text
                print("Input finale:", self.saved_text)
            else:
                self.text += event.unicode

    def update(self):
        # Aggiornamento del cursore lampeggiante
        self.cursor_counter += 1
        if self.cursor_counter >= 30:
            self.cursor_counter = 0
            self.cursor_visible = not self.cursor_visible

    def draw(self, screen):
        # Disegna il campo di input
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  # Bordo nero

        # Disegna il testo
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        # Disegna il cursore lampeggiante se attivo
        if self.cursor_visible and self.active:
            cursor_x = self.rect.x + 5 + text_surface.get_width()
            pygame.draw.line(screen, self.text_color, (cursor_x, self.rect.y + 5), (cursor_x, self.rect.y + self.rect.height - 5), 2)