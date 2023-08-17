import pygame as pg
import sys
from main_hero import Hero


def game():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    player = Hero(100, 100)

    while True:
        screen.fill((0, 0, 0))
        player.draw(screen)
        pg.display.flip()

        clock.tick(60) #FPS

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


WIDTH = 500
HEIGHT = 400
BACKGROUND = (0, 0, 0)

if __name__ == '__main__':
    game()
