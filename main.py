import pygame as pg
from pygame import time


M = 2
G = 10


class Space:    # пространство
    def __init__(self, width, height):
        """Инициализация поля"""
        # Ширина поля:
        self.width = 800
        # Высота поля:
        self.height = 800
        # Размер ячейки:
        self.cell_size = 25
        # Изначально заполняем игровое поле нулями:
        self.board = [[0] * (width // self.cell_size) for _ in range(height // self.cell_size)]
        # Отступ сверху:
        self.top = 0
        # Отступ слева:
        self.left = 200

    def render(self):
        """Рендеринг"""
        # Рисуем клетчатое поле:
        self.board[3][6] = 1
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    pg.draw.rect(screen,
                                 pg.Color(0, 170, 114, 100),
                                 (j * self.cell_size + self.left,
                                 i * self.cell_size + self.top,
                                 self.cell_size, self.cell_size), 1)
                if self.board[i][j] == 1:
                    pg.draw.rect(screen,
                                 pg.Color(0, 170, 114, 100),
                                 (j * self.cell_size + self.left,
                                 i * self.cell_size + self.top,
                                 self.cell_size, self.cell_size))

    def random_level(self, diff, maxi):
        pass


class Plateau:   # плато
    pass


class Jumper(pg.sprite.Sprite):    # прыгун
    # bomb = load_image('bomb.png')  # бомбочка
    # boom = load_image('boom.png')  # взрыв

    def __init__(self, group):
        super().__init__(group)

    def update(self, *args):
        """Функция обновления группы спрайтов"""
        # Посмотрим в терминале,
        # какие аргументы передаются при возникновении события:
        if args:
            print(args)

        # прыжок:

        # столкновение


def move_jumper(player, movement):
    x, y = player.pos


if __name__ == '__main__':
    pg.init()
    size = width, height = 1200, 800
    screen = pg.display.set_mode(size)
    pg.draw.rect(screen, (255, 255, 255), [200, 0, width - 400, height])
    board = Space(800, 800)
    running = True
    clock = time.Clock()
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pg.event.get():
            # при закрытии окна
            if event.type == pg.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        # ...
        board.render()
        # обновление экрана
        pg.display.flip()
        clock.tick(100)
    pg.quit()