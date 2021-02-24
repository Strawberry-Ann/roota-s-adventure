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
        self.speedy = -4
        self.G = 0.002
        self.rect = pg.Rect(x, y, 10, 10)
        self.image = Roota.image
        print(x, y, *group)
        self.add(roota_sprites)

    def update(self, dt, size):
        if self.rect[x1] < 0:
            self.rect[x1] += size
        self.rect[x1] = (self.rect[x1] + self.speedx) % size
        self.rect[y1] += self.speedy
        self.speedy = self.speedy + self.G * dt

    def speed_up(self):
        self.speedy = -4


class Stick(pg.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.speedy = 0.4
        self.G = 0.002
        self.rect = pg.Rect(pos[0], pos[1], 30, 5)

    def update(self):
        self.rect[y1] += self.speedy

    def speed_up(self):
        self.speedy = 0.4


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Dodle Jump')
    size = width, height = 350, 700
    screen = pg.display.set_mode(size)
    screen.fill((0, 0, 0))
    roota_sprites = pg.sprite.Group()
    sticks = pg.sprite.Group()
    hero = Roota(100, 600)
    running = True
    clock = time.Clock()
    while running:
        screen.fill(pg.Color('black'))
        roota_sprites.draw(screen)
        roota_sprites.update(time.get_ticks(), 350)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEMOTION:
                x1, y1 = event.pos
        pg.display.flip()
        clock.tick(100)
    pg.quit()