# https://programmers.co.kr/learn/courses/4008/lessons/12837

class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f'({self.x}, {self.y})'

point = Coord(1, 2)
print(point)