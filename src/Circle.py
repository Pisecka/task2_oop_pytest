import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius







c1 = Circle('circle1', 10)