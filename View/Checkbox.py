import pygame

class Checkbox:
    def __init__(self, x, y, size, color=(255,255,255), checked_color=(0,255,0)):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.checked_color = checked_color
        self.checked = False

    def draw(self, surface):
        # Disegna il contorno della checkbox
        pygame.draw.rect(surface, self.color, self.rect, 2)
        # Disegna il riempimento se è selezionata
        if self.checked:
            pygame.draw.rect(surface, self.checked_color, self.rect.inflate(-4, -4))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Sinistro del mouse
                if self.rect.collidepoint(event.pos):
                    self.checked = not self.checked