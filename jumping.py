import pygame as pg
from random import randrange, choices, choice
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
    image1 = load_image('hero.png')
    image2 = load_image('hero2.png')

    def __init__(self, x, y):
        super().__init__(group_sprites)
        self.speedx = 0
        self.speedy = -2
        self.G = 0.02
        self.rect = pg.Rect(x, y, 28, 50)
        self.image = Roota.image1
        self.mask = pg.mask.from_surface(self.image)
        self.add(roota_sprites)
        self.dt = 0

    def speed_up(self):
        self.speedy = -2
        self.dt = time.get_ticks() // 1000

    def update(self):
        dt = time.get_ticks() // 1000 - self.dt
        if self.rect.x < 200:
            self.rect.x += 800
        self.rect.x = (self.rect.x + self.speedx) % size[0]
        self.rect.y += self.speedy
        self.speedy = self.speedy + self.G * dt
        if pg.sprite.spritecollideany(self, horizontal_borders):
            self.speed_up()
        if self.speedy >= 0:
            self.image = Roota.image1
            self.mask = pg.mask.from_surface(self.image1)
            if pg.sprite.spritecollideany(self, sticks):
                self.speed_up()
        else:
            self.image = Roota.image2
            self.mask = pg.mask.from_surface(self.image)

    def speed_up_x(self, coord_x):
        self.speedx = (coord_x - self.rect.x - (self.rect.width // 2)) // 100


class Stick(pg.sprite.Sprite):
    image = load_image("stick.jpg")

    def __init__(self, x, y):
        super().__init__(group_sprites)
        self.add(sticks)
        self.speedy = 0
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
        self.rect = pg.Rect(200, 0, 1000, 600)


class Level:
    def __init__(self, minx, miny, maxx, maxy, sizex, sizey):
        self.minx, self.miny = minx, miny
        self.maxx, self.maxy = maxx, maxy
        self.sizex, self.sizey = sizex, sizey
        self.level = list()
        self.add_sticks()

    def add_sticks(self):
        c = 1
        for i in range(self.sizey, self.miny, (self.miny // 2)):
            if choice([0, 1]) == 1 or c == 1:
                h = i - randrange(0, self.maxy - self.miny + 1)
                m1 = randrange(1, self.sizex // self.minx - 1)
                m2, m3 = randrange(m1, (self.sizex // self.minx)), randrange(0, m1)
                t = choices([0, 1, 2], k=2)
                for k in [(0, m1), (1, m2), (2, m3)]:
                    if k[0] in t:
                        self.level.append((k[1] * self.minx + 200, h + 550))
                c = 0
            else:
                c = 1


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Dodle Jump')
    size = width, height = 1200, 600
    screen = pg.display.set_mode(size)
    screen.fill((0, 0, 0))
    group_sprites = pg.sprite.Group()
    Background()
    roota_sprites = pg.sprite.Group()
    sticks = pg.sprite.Group()
    level = Level(20, 150, 200, 350, 800, -5000)
    for x, y in level.level:
        Stick(x, y)
    horizontal_borders = pg.sprite.Group()
    hero = Roota(500, 550)
    Border(5, height - 5, width - 5, height - 5)
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