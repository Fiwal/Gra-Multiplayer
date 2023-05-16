import pygame
from pygame.locals import *

class Pickup:
    def __init__(self, x, y, size):
        self.rect = Rect(x, y, size, size)
        self.color = (255, 255, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)