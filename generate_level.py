from random import randrange, choice


class Level:
    def __init__(self, minx, miny, maxx, maxy, sizex, sizey):
        self.minx, self.miny = minx, miny
        self.maxx, self.maxy = maxx, maxy
        self.sizex, self.sizey = sizex, sizey
        self.level = list()

    def add_sticks(self):
        for i in range(self.miny, self.sizey, self.maxy):
            h = i - randrange(0, self.maxy - self.miny)
            t = 1
            for j in range(1, self.sizex // self.minx):
                if choice(0, 1) == 1 or t == 1:
                    w = j * (self.maxx) - randrange(0, self.maxx - self.minx)
                    if t == 1:
                        t = 0
                    self.level.append((w, h))
