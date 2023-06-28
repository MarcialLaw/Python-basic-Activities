from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return "(" + str(self.x) +"," + str(self.y) + ")"

p = Point(3, -4)
q = Point(5, 7)
print(str(p))
p.translate(1, 5)
print(p)
print(p.distance(q))
Point.translate(p, 1, 5)
print(p)
print(q)
p=q
print(p)
     
