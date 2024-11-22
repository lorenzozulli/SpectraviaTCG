import pygame
import sys

class DropdownMenu:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)

    def __init__(self, x, y, width, height, font, options, default_text="Seleziona"):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.options = options
        self.default_text = default_text
        self.selected_option = default_text
        self.is_open = False
        self.option_rects = []

    def draw(self, screen):
        # Disegna il bottone del dropdown
        pygame.draw.rect(screen, self.GRAY, self.rect)
        text = self.font.render(self.selected_option, True, self.BLACK)
        screen.blit(text, (self.rect.x + 10, self.rect.y + 10))

        if self.is_open:
            self.option_rects = []
            # Disegna le opzioni
            for idx, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + (idx + 1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(screen, self.WHITE, option_rect)
                text = self.font.render(option, True, self.BLACK)
                screen.blit(text, (option_rect.x + 10, option_rect.y + 10))
                self.option_rects.append(option_rect)
        else:
            self.option_rects.clear()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if self.rect.collidepoint(pos):
                # Toggle del menu a tendina
                self.is_open = not self.is_open
            elif self.is_open:
                for idx, rect in enumerate(self.option_rects):
                    if rect.collidepoint(pos):
                        self.selected_option = self.options[idx]
                        self.is_open = False
                        break