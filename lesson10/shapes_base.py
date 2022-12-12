import math
from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, units: str, color: str):
        self._units = units
        self._color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, units, color, a, b, c):
        super().__init__(units, color)
        self._a = a
        self._b = b
        self._c = c
        self._is_valid = a + b > c and b + c > a and a + c > b
        if not self._is_valid:
            raise Exception


class Rectangle(Shape):
    def __init__(self, units, color, height, width):
        super().__init__(units, color)
        self._height = height
        self._width = width

    def area(self):
        return self._height * self._width

    def perimeter(self):
        return 2 * self._height + 2 * self._width


class Circle(Shape):
    def __init__(self, units, color, radius):
        super().__init__(units, color)
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2

    def perimeter(self):
        return 2 * math.pi * self._radius


rect = Rectangle('cm', 'red', 3, 5)
print(rect.area())
print(rect.perimeter())

circ = Circle('mm', 'black', 5)
print(circ.area())
print(circ.perimeter())
