import pygame as pg
import sys
from main_hero import Hero
from wood import Box


def game():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    player = Hero(100, 400)

    boxes = pg.sprite.Group()

    for box in range(0, 400, 50):
        boxes.add(Box(box, 500))

    while True:
        screen.fill(BACKGROUND)

        player.update(boxes)
        player.draw(screen)
        boxes.draw(screen)

        print(player.gravity)
        print(player.vertical_speed)

        pg.display.flip()
        clock.tick(60)  # FPS

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


WIDTH = 380
HEIGHT = 500
BACKGROUND = (0, 0, 0)

if __name__ == '__main__':
    game()
