import pygame as pg
from random import randrange
from pygame import time
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


class Roota(pg.sprite.Sprite):
    image = load_image('hero.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.speedx = 0
        self.speedy = -1
        self.G = 0.02
        self.rect = pg.Rect(x, y, 10, 10)
        self.image = Roota.image
        print(x, y, *group)
        self.add(roota_sprites)

    def speed_up(self):
        self.speedy = -1

    def update(self, dt, size):
        if self.rect.x < 0:
            self.rect.x += size[0]
        self.rect.x = (self.rect.x + self.speedx) % size[0]
        if self.rect.y - self.rect.height - 1 == size[1]:
            self.speed_up()
        self.rect.y += self.speedy
        self.speedy = self.speedy + self.G * dt
        print(self.rect.x, self.rect.y)


class Stick(pg.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.speedy = 1
        self.G = 0.02
        self.rect = pg.Rect(x, y, 30, 5)

    def update(self):
        self.rect.y += self.speedy

    def speed_up(self):
        self.speedy = 1


class Border(pg.sprite.Sprite):
    """Ограничивающая рамка"""
    def __init__(self, x1, y1, x2, y2):
        super().__init__(group_sprites)
        if y1 == y2:
            self.add(horizontal_borders)
            self.image = pg.Surface((x2 - x1, 1))
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Dodle Jump')
    size = width, height = 350, 700
    screen = pg.display.set_mode(size)
    screen.fill((0, 0, 0))
    group_sprites = pg.sprite.Group()
    roota_sprites = pg.sprite.Group()
    sticks = pg.sprite.Group()
    border = pg.sprite.Group()
    horizontal_borders = pg.sprite.Group()
    hero = Roota(100, 600)
    running = True
    clock = time.Clock()
    while running:
        screen.fill(pg.Color('black'))
        roota_sprites.draw(screen)
        roota_sprites.update(time.get_ticks() // 1000, size)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEMOTION:
                x1, y1 = event.pos
        pg.display.flip()
        clock.tick(100)
    pg.quit()