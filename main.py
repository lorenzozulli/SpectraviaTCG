import pygame
from Model.Network import Network

pygame.init()

SCREEN_WIDTH = 1360
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Client")
# Quando avro' un icona pygame.display.set_icon("")

clientNumber = 0

def redrawWindow():
    screen.fill((255,255,255))
    pygame.display.update()


def main():
    run = True
    n = Network()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        redrawWindow()

main()
                