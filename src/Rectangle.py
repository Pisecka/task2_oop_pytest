from src.Figure import Figure
from src.Circle import Circle

class Rectangle(Figure):

    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return self.a * 2 + self.b  * 2




r1 = Rectangle('rect1', 5, 10)
c1 = Circle('circle1', 10)