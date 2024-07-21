import math
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_square(self):
        return 0.0

    @abstractmethod
    def validation(self):
        pass


class Circle(Figure):
    def __init__(self, R):
        super().__init__()
        self.R = R
        self.validation()

    def get_square(self):
        return math.pi * self.R * self.R

    def validation(self):
        if self.R <= 0:
            raise ValueError('Радиус должен быть положительным числом')


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.validation()
        self.p = None

    def get_square(self):
        if not self.p:
            self.p = (self.a + self.b + self.c) / 2
        return (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** (1 / 2)

    def validation(self):
        self.positive_sides()
        self.aspect_ratio()

    def positive_sides(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError('Все стороны треугольника должны быть положительными числами')

    def aspect_ratio(self):
        if self.a >= self.b + self.c or self.b >= self.c + self.a or self.c >= self.b + self.a:
            raise ValueError('Не выполняется условие соотношения сторон треугольника')

    def is_rectangular(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2


if __name__ == '__main__':
    figures = [Circle(5), Triangle(5, 5, 5)]
    for figure in figures:
        figure: Figure
        print(figure.get_square())

    t = Triangle(3, 4, 5)
    print(t.is_rectangular())
