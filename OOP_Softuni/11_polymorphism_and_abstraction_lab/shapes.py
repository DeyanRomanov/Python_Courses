import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self):
        return self.side_a * self.side_b

    def calculate_perimeter(self):
        return (self.side_a * 2) + (self.side_b * 2)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_perimeter(self):
        return 2 * math.pi * self.r

    def calculate_area(self):
        return math.pi * (self.r ** 2)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
