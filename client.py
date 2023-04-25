import pygame
from pygame.locals import *
from pygame.constants import *
from network import Network

WIDTH = 800
HEIGHT = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

clientNumber = 0


def redraw_window(p, p2):
    screen.fill((0, 0, 0))
    p.draw(screen)
    p2.draw(screen)
    pygame.display.update()
    clock.tick(60)


def main():
    run = True
    n = Network()
    p = n.get_player()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            p.move(0, -2)
        if keys[K_s]:
            p.move(0, 2)
        if keys[K_a]:
            p.move(-2, 0)
        if keys[K_d]:
            p.move(2, 0)

        p.update()

        p2 = n.send(p)

        redraw_window(p, p2)


if __name__ == "__main__":
    main()
