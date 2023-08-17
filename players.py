import pygame as pg


class Sprit(pg.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self) -> None:
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)