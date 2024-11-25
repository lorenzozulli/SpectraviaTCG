### -------------------------------------------- ###
import pygame
### -------------------------------------------- ###

class Checkbox():
    def __init__(self, x, y, size, text, font_size=30, text_color=(0,0,0),color=(255,255,255), checked_color=(0,255,0)):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.checked_color = checked_color
        self.text = text
        self.checked = False

    def draw(self, screen):
        # Disegna il contorno della checkbox
        pygame.draw.rect(screen, self.color, self.rect, 2)

        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        
        # Disegna il riempimento se è selezionata
        if self.checked:
            pygame.draw.rect(screen, self.checked_color, self.rect.inflate(0,0))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Sinistro del mouse
                if self.rect.collidepoint(event.pos):
                    self.checked = not self.checked