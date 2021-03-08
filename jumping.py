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
        self.speedy = -1
        self.G = 0.01
        self.rect = pg.Rect(x, y, 28, 50)
        self.image = Roota.image1
        self.mask = pg.mask.from_surface(self.image)
        self.add(roota_sprites)
        self.dt = 0
        self.stopx = x

    def speed_up(self):
        self.speedy = -1
        self.dt = time.get_ticks() // 1000

    def update(self):
        dt = time.get_ticks() // 1000 - self.dt
        if self.rect.x <= 200:
            self.rect.x += 800
        if self.rect.x >= 1000:
            self.rect.x -= 800
        if self.rect.x == self.stopx:
            self.speedx = 0
        self.rect.x = (self.rect.x + self.speedx) % size[0]
        self.rect.y += self.speedy
        self.speedy = self.speedy + self.G * dt
        if pg.sprite.spritecollideany(self, horizontal_borders):
            self.speed_up()
        if self.speedy >= 1:
            self.image = Roota.image1
            self.mask = pg.mask.from_surface(self.image1)
            if pg.sprite.spritecollideany(self, sticks):
                self.speed_up()
        else:
            self.image = Roota.image2
            self.mask = pg.mask.from_surface(self.image)

    def speed_up_x(self, coord_x):
        self.speedx = (coord_x - self.rect.x - (self.rect.width // 2)) // 25
        # задаём значение координаты по икс, достигнув которого,
        # спрайт перестанет перемещаться по оси икс
        self.stopx = coord_x


class Stick(pg.sprite.Sprite):
    image = load_image("stick.jpg")

    def __init__(self, x, y):
        super().__init__(group_sprites)
        self.add(sticks)
        self.speedy = 1
        self.G = 0.02
        self.timer = False
        self.time_rewind = 0
        self.rect = pg.Rect(x, y, 30, 5)

    def update(self):
        self.rect.y += self.speedy
        self.speed_up
        if hero.rect.y <= 0:
            self.timer = True
            self.time_rewind = time.get_ticks()
        if self.timer:
            self.time = self.time_rewind - time.get_ticks()
            if self.time <= 3000:
                self.timer = False
                self.speedy = 1
            else:
                pass

    def speed_up(self):
        self.speedy = 1


class Coin(pg.sprite.Sprite):
    """Анимированный спрайт"""
    def __init__(self, sheet, cols, rows, x, y):
        super().__init__(group_sprites)
        # frames - атрибут класса,
        # список для хранения последовательности кадров спрайта:
        self.frames = []
        # Разрезаем лист на кадры,
        # используя функцию cut_sheet() из данного класса (см. ниже):
        self.cut_sheet(sheet, cols, rows)
        # Обнуляем номер текущего кадра:
        self.cur_frame = 0
        # image - атрибут класса,
        # в который помещаем текущий кадр:
        self.image = self.frames[self.cur_frame]
        self.mask = pg.mask.from_surface(self.image)
        # Помещаем прямоугольник с кадром в координаты (x, y):
        self.rect = self.rect.move(x, y)
        self.speedy = 1

    def cut_sheet(self, sheet, cols, rows):
        """Функция разрезания листа с кадрами спрайта"""
        # Задаём маленький прямоугольник размером с кадр:
        self.rect = pg.Rect(0, 0, sheet.get_width() // cols, sheet.get_height() // rows)
        # Пробегаем по всем кадрам спрайта:
        for j in range(rows):
            for i in range(cols):
                # Определяем координаты кадра на листе:
                frame_location = (self.rect.w * i, self.rect.h * j)
                # Копируем кадр из листа в список frames, используя метод subsurface(),
                # который возвращает новую поверхность с нарисованным на ней кадром:
                self.frames.append(sheet.subsurface(pg.Rect(frame_location, self.rect.size)))

    def update(self):
        self.rect.y += self.speedy
        # """Смена кадра спрайта"""
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.mask = pg.mask.from_surface(self.image)
        if pg.sprite.spritecollideany(self, roota_sprites):
            self.kill()


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
    def __init__(self, miny, sizey):
        self.miny = miny
        self.sizey = sizey
        self.level = list()
        self.add_sticks()

    def add_sticks(self):
        y = self.sizey
        while y < 600:
            x = randrange(0, 600)
            x += 200
            Stick(x, y)
            Coin(sheet_coin, 4, 1, x - 5, y - 54)
            y += 50


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
    sheet_coin = load_image("coin.png")
    level = Level(50, -5000)
    horizontal_borders = pg.sprite.Group()
    hero = Roota(500, 550)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, -5000, width - 5, -5000)
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