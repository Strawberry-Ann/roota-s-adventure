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

    def __init__(self, x, y):
        super().__init__(group_sprites)
        self.speedx = 0
        self.speedy = -2
        self.G = 0.02
        self.rect = pg.Rect(x, y, 28, 50)
        self.image = Roota.image
        self.mask = pg.mask.from_surface(self.image)
        self.add(roota_sprites)
        self.dt = 0

    def speed_up(self):
        self.speedy = -2
        self.dt = time.get_ticks() // 1000

    def update(self):
        dt = time.get_ticks() // 1000 - self.dt
        if self.rect.x < 0:
            self.rect.x += size[0]
        self.rect.x = (self.rect.x + self.speedx) % size[0]
        self.rect.y += self.speedy
        self.speedy = self.speedy + self.G * dt
        if pg.sprite.spritecollideany(self, horizontal_borders):
            self.speed_up()
        if self.speedy > 0:
            if pg.sprite.spritecollideany(self, sticks):
                self.speed_up()

    def speed_up_x(self, coord_x):
        self.speedx = (coord_x - self.rect.x - (self.rect.width // 2)) // 100


class Stick(pg.sprite.Sprite):
    image = load_image("stick.jpg")

    def __init__(self, x, y):
        super().__init__(group_sprites)
        self.add(sticks)
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


class Background(pg.sprite.Sprite):
    """фон"""
    image = load_image("screen.jpg")

    def __init__(self):
        super().__init__(group_sprites)
        self.rect = pg.Rect(0, 0, 350, 700)


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Dodle Jump')
    size = width, height = 350, 700
    screen = pg.display.set_mode(size)
    screen.fill((0, 0, 0))
    group_sprites = pg.sprite.Group()
    roota_sprites = pg.sprite.Group()
    sticks = pg.sprite.Group()
    horizontal_borders = pg.sprite.Group()
    Background()
    hero = Roota(100, 600)
    Border(5, height - 5, width - 5, height - 5)
    Stick(85, 100)
    running = True
    clock = time.Clock()
    while running:
        screen.fill(pg.Color('black'))
        group_sprites.draw(screen)
        group_sprites.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEMOTION:
                x1, y1 = event.pos
                if 0 < x1 < width and 0 < y1 < height:
                    hero.speed_up_x(x1)
        pg.display.flip()
        clock.tick(100)
    pg.quit()