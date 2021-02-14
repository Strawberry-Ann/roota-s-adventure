import pygame as pg


class Space:    # пространство
    pass


class Plateau:   # плато
    pass


class Jumper:    # прыгун
    pass


if __name__ == '__main__':
    pg.init()
    size = width, height = 1200, 800
    screen = pg.display.set_mode(size)
    pg.draw.rect(screen, (255, 255, 255), [200, 0, width - 400, height])

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pg.event.get():
            # при закрытии окна
            if event.type == pg.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pg.display.flip()
    pg.quit()