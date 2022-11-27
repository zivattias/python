import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __add__(self, other):
        if not isinstance(other, Point2D):
            return f'{other} is not a Point'
        return Point2D(self.x + other.x, self.y + other.y)


if __name__ == '__main__':
    p1 = Point2D()
    p2 = Point2D(2, 5)
    print(p1, p2)
    p2.translate(-2, -2)
    p1.translate(3, 3)
    print(p1)
    print(p2)
    p3 = Point2D(0, 3)
    print(p2 == p3)
    print(p2 == 'hello')
    print(p2)
    print(p3)
    new_point = p2 + p3
    print(f'new point: {new_point}')
    print(p2)
    print(p3)
    print(p1)
    other_point = p2 + p3 + p1
    print(f'other point: {other_point}')
