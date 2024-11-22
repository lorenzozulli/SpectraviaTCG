import pygame

class DropdownMenu:
    def __init__(self, x, y, size, font_size=30, text_color=(0,0,0)):
        self.rect = pygame.Rect(x, y, size, size)
    # Funzione per disegnare il menu
    def draw(self, screen):
        # Disegna il bottone del dropdown
        pygame.draw.rect(screen, GRAY, dropdown_rect)
        text = font.render(selected_option, True, BLACK)
        screen.blit(text, (dropdown_rect.x + 10, dropdown_rect.y + 10))

        if is_open:
            # Disegna le opzioni
            for idx, option in enumerate(options):
                option_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (idx + 1) * 40, dropdown_rect.width, 40)
                pygame.draw.rect(screen, WHITE, option_rect)
                text = font.render(option, True, BLACK)
                screen.blit(text, (option_rect.x + 10, option_rect.y + 10))
                option_rects.append(option_rect)
        else:
            option_rects.clear()

    # Funzione per gestire il clic sulle opzioni
    def handle_event(pos):
        global selected_option, is_open
        if dropdown_rect.collidepoint(pos):
            # Toggle del menu a tendina
            is_open = not is_open
        elif is_open:
            for idx, rect in enumerate(option_rects):
                if rect.collidepoint(pos):
                    selected_option = options[idx]
                    is_open = False
                    break