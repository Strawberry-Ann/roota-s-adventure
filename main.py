import pygame as pg


class Space:    # пространство
    def __init__(self, width, height):
        """Инициализация поля"""
        # Ширина поля:
        self.width = 800
        # Высота поля:
        self.height = 800
        # Изначально заполняем игровое поле нулями:
        self.board = [[0] * width for _ in range(height)]
        # Отступ сверху:
        self.top = 0
        # Отступ слева:
        self.left = 200
        # Размер ячейки:
        self.cell_size = 50

    def render(self):
        """Рендеринг"""
        # Рисуем клетчатое поле:
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pg.draw.rect(screen,
                                 pg.Color('black'),
                                 (x * self.cell_size + self.left,
                                 y * self.cell_size + self.top,
                                 self.cell_size, self.cell_size), 0)

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


if __name__ == '__main__':
    pg.init()
    size = width, height = 1200, 800
    screen = pg.display.set_mode(size)
    pg.draw.rect(screen, (255, 255, 255), [200, 0, width - 400, height])
    board = Space(800, 800)
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
        board.render()
        # обновление экрана
        pg.display.flip()
    pg.quit()