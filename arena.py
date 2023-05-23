import pygame
from pygame.locals import Rect


class Arena:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x, self.y, self.width, self.height)



    def check_collision(self, object):
        isColliding = False
        if object.x < self.x:
            object.x = self.x
            object.velX = 0
            isColliding = True

        if object.y < self.y:
            object.y = self.y
            object.velY = 0
            isColliding = True

        if object.x + object.width > self.x + self.width:
            object.x = self.x + self.width - object.width
            object.velX = 0
            isColliding = True

        if object.y + object.height > self.y + self.height:
            object.y = self.y + self.height - object.height
            object.velY = 0
            isColliding = True

        return isColliding

    def draw(self, screen, camera):
        self.drawRect = Rect(self.x - camera.x, self.y - camera.y, self.width, self.height)
        pygame.draw.rect(screen, (0, 0, 0), self.drawRect)
