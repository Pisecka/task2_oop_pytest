from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c)/2
        S= (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return S

    def perimeter(self):
        return self.a + self.b + self.c




t1 = Triangle('triangle', 7, 10, 15)