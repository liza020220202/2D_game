from players import Sprit
import pygame


class Hero(Sprit):
    def __init__(self, startx, starty):
        super().__init__('hero11.png', startx, starty)

        self.stand_image = self.image

        self.speed = 4
        self.jump = 20
        self.vertical_speed = 0
        self.gravity = 1

    def update(self, boxes) -> None:
        horizontal_speed = 0
        onground = pygame.sprite.spritecollideany(self, boxes)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            horizontal_speed = -self.speed
        if key[pygame.K_RIGHT]:
            horizontal_speed = self.speed

        if key[pygame.K_UP] and onground:
            self.vertical_speed = -self.jump
        if self.vertical_speed < 10 and not onground:
            self.vertical_speed += self.gravity
        if self.vertical_speed >= 0 and onground:
            self.vertical_speed = 0

        self.move(horizontal_speed, self.vertical_speed)

    def move(self, x, y):
        self.rect.move_ip([x, y])

    def walk_animation(self):
        pass