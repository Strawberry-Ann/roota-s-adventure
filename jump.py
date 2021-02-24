import pygame as pg
from random import randrange
from pygame import time


def roots_of_quadratic_equation(a, b, c):
    x = list()
    if a != 0:
        d = b ** 2 - 4 * a * c
        if d == 0:
            x.append((- b) // 2 // a)
        elif d > 0:
            x.append((-b + d ** (1 / 2)) // 2 // a)
            x.append((-b - d ** (1 / 2)) // 2 // a)
    elif a == 0 and b == 0 and c == 0:
        x.append('all')
    elif a == 0 and b != 0:
        x.append((-c) / b)
    return x


def get_Vx(x0, x1, t):
    Vx = (x1 - x0) // t
    return Vx


def jump(x0, y0, Vx, Vy, t):
    y = y0 - Vy + 10
    x = x0 + Vx
    return int(x), int(y)


def get_t(y0, y, Vy, t):
    r = roots_of_quadratic_equation(5,  Vy, (y0 - y))
    print(r)
    all_t = list(filter(lambda x: x >= 0, roots_of_quadratic_equation(5,  Vy, (y0 - y))))[0]
    return int(all_t) - t


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Шарик')
    size = width, height = 300, 300
    screen = pg.display.set_mode(size)
    screen.fill((0, 0, 0))
    x0, y0 = 10, height - 11
    x, y = 10, height - 11
    Vx, Vy = 1, 1
    t = time.get_ticks()
    running = True
    clock = time.Clock()
    screen.fill(pg.Color('black'))
    while running:
        screen.fill(pg.Color('black'))
        pg.draw.circle(screen, (255, 255, 255), (x, y), 10)
        if y == height - 10:
            x0, y0 = x, y
            Vy = 1
            t = time.get_ticks()
        x, y = jump(x0, y0, Vx, Vy, (time.get_ticks() - t))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEMOTION:
                x1, y1 = event.pos
                #  Vx = get_Vx(x0, x1, get_t(y0, y, Vy, time.get_ticks() - t))
        pg.display.flip()
        clock.tick(1000)
    pg.quit()