from src.Figure import Figure


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
