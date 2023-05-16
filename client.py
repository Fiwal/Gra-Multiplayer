import pygame
from pygame.constants import *
from network import Network

pygame.init()

WIDTH = 800
HEIGHT = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

clientNumber = 0

text_font = pygame.font.SysFont("Helvetica", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def redraw_window(players, pickups, score):
    screen.fill((0, 0, 0))
    for player in players:
        player.draw(screen)

    for pickup in pickups:
        pickup.draw(screen)

    textToShow = f"Points: {score}"
    draw_text(textToShow, text_font, (255, 255, 255), 20, 20)
    pygame.display.update()
    clock.tick(60)



def main():
    run = True
    n = Network()
    pickups = n.send("pickups")
    score = 0
    p = n.get_player()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            p.move(0, -7)
        if keys[K_s]:
            p.move(0, 7)
        if keys[K_a]:
            p.move(-7, 0)
        if keys[K_d]:
            p.move(7, 0)

        left, middle, right = pygame.mouse.get_pressed()

        if left:
            p.x, p.y = pygame.mouse.get_pos()

        if right:
            p.width += 1
            p.height += 1

        if middle:
            p.width -= 1
            p.height -= 1

        p.update()
        pickups = n.send("pickups")
        all_players = n.send(p)
        score = n.send("score")
        redraw_window(all_players, pickups, score)


if __name__ == "__main__":
    main()
