from random import randrange, choice, choices


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
                        self.level.append((k[1] * self.minx, h))
                c = 0
            else:
                c = 1