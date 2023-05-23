import pygame
from pygame.locals import *

class Pickup:
    def __init__(self, x, y, size):
        self.drawRect = None
        self.rect = Rect(x, y, size, size)
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 255, 0)

    def draw(self, screen, camera):
        self.drawRect = Rect(self.x - camera.x, self.y - camera.y, self.size, self.size)
        pygame.draw.rect(screen, (255, 255, 0), self.drawRect)