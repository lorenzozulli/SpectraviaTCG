import pygame

pygame.init()

SCREEN_WIDTH = 1360
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Client")

clientNumber = 0

def redrawWindow():
    run = True
    while run:
        screen.fill((255,255,255))
        pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        redrawWindow()
                