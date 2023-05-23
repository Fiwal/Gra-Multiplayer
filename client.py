import pygame
from pygame.locals import *
from pygame.constants import *

from offsetManager import OffsetManager
from network import Network
from bullet import Bullet

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Client")

text_font = pygame.font.SysFont("Helvetica", 30)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def redraw_window(players, pickups, bullets, score, arena, camera):
    screen.fill((100, 100, 100))
    arena.draw(screen, camera)
    for player in players:
        player.draw(screen, camera)

    for pickup in pickups:
        pickup.draw(screen, camera)

    for bullet in bullets:
        bullet.draw(screen, camera)

    textToShow = f"Points: {score}"
    draw_text(textToShow, text_font, (255, 255, 255), 20, 20)
    pygame.display.update()
    clock.tick(60)


def main():

    camera = OffsetManager()
    run = True
    n = Network()
    arena = n.send("arena")
    pickups = n.send("pickups")

    score = 0

    p = n.get_player()
    all_players = [p]
    bullets = []


    p.update()
    mousePos = pygame.mouse.get_pos()
    centerOfPlayer = p.x + p.width / 2 - SCREEN_WIDTH, p.y + p.height / 2 - SCREEN_HEIGHT
    cameraPos = (mousePos[0] + centerOfPlayer[0]), (mousePos[1] + centerOfPlayer[1])
    camera.setOffset(cameraPos[0], cameraPos[1])
    print(mousePos)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                newX, newY = pygame.mouse.get_pos()
                newBullet = make_bullet(camera, newX, newY, p)
                bullets = n.send(newBullet)

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            p.move(0, -0.5)
        if keys[K_s]:
            p.move(0, 0.5)
        if keys[K_a]:
            p.move(-0.5, 0)
        if keys[K_d]:
            p.move(0.5, 0)


        p.update()
        mousePos = pygame.mouse.get_pos()
        centerOfPlayer = p.x + p.width / 2 - SCREEN_WIDTH, p.y + p.height / 2 - SCREEN_HEIGHT
        cameraPos = (mousePos[0] + centerOfPlayer[0]), (mousePos[1] + centerOfPlayer[1])

        camera.setOffset(cameraPos[0],  cameraPos[1])
        arena.check_collision(p)
        all_players = n.send(p)
        pickups = n.send("pickups")
        score = n.send("score")
        bullets = n.send("bullets")
        p = n.send("hitByBullet")

        redraw_window(all_players, pickups, bullets, score, arena, camera)


def make_bullet(camera,newX, newY, p):
    # Startowanie od środka gracza
    mouseVector = newX + camera.x - (p.x + p.width / 2), newY - (p.y + p.height / 2) + camera.y
    length = (mouseVector[0] ** 2 + mouseVector[1] ** 2) ** 0.5
    normVector = mouseVector[0] / length, mouseVector[1] / length
    velocity = 20
    newBullet = Bullet(p.x + p.width / 2, p.y + p.height / 2, normVector[0] * velocity, normVector[1] * velocity,
                       (255, 255, 255), p)
    return newBullet


if __name__ == "__main__":
    main()
