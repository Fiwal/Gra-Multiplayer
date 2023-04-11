import pygame
from pygame.locals import *
from pygame.constants import *

WIDTH = 800
HEIGHT = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

clientNumber = 0

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = color

        self.rect = Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.rect = Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, x, y):
        self.x += x
        self.y += y


def redraw_window(player):
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.update()
    clock.tick(60)


def main():
    run = True
    player = Player(100, 100, 50, 50, (200, 0, 0))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            player.move(0, -2)
        if keys[K_s]:
            player.move(0, 2)
        if keys[K_a]:
            player.move(-2, 0)
        if keys[K_d]:
            player.move(2, 0)

        player.update()


        redraw_window(player)

if __name__ == "__main__":
    main()
