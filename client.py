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

def read_pos(text):
    text = text.split(",")
    return int(text[0]), int(text[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

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


def redraw_window(p, p2):
    screen.fill((0, 0, 0))
    p.draw(screen)
    p2.draw(screen)
    pygame.display.update()
    clock.tick(60)


def main():
    run = True
    n = Network()
    startPos = read_pos(n.get_pos())
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0))

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
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        redraw_window(p, p2)


if __name__ == "__main__":
    main()
