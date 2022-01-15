from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b