from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c