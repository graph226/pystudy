from math import cos, sin, pi

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

def koch_pos(n, a, b):
    if n == 0:
        return
    th = pi * 60.0 / 180.0

    s, t, u = Point(0.0, 0.0), Point(0.0, 0.0), Point(0.0, 0.0)
    s.x = (2.0 * a.x + 1.0 * b.x) / 3.0
    s.y = (2.0 * a.y + 1.0 * b.y) / 3.0
    t.x = (1.0 * a.x + 2.0 * b.x) / 3.0
    t.y = (1.0 * a.y + 2.0 * b.y) / 3.0
    u.x = (t.x - s.x) * cos(th) - (t.y - s.y) * sin(th) + s.x
    u.y = (t.x - s.x) * sin(th) + (t.y - s.y) * cos(th) + s.y

    for pos in koch_pos(n - 1, a, s):
        yield pos
    yield s.x, s.y
    for pos in koch_pos(n - 1, s, u):
        yield pos
    yield u.x, u.y
    for pos in koch_pos(n - 1, u, t):
        yield pos
    yield t.x, t.y
    for pos in koch_pos(n - 1, t, b):
        yield pos


def koch(n, a, b):
    yield a.x, a.y
    for pos in koch_pos(n, a, b):
        yield pos
    yield b.x, b.y

if __name__ == "__main__":
    from turtle import *
    a = Point(-500.0, 0.0)
    b = Point(500.0, 0.0)
    n = 5
    t = Turtle()

    first = True
    for x, y in koch(n, a, b):
        if first:
            first = False
            t.penup()
            t.setpos(x, y)
            t.pendown()
        else:
            t.setpos(x, y)

    exitonclick()
