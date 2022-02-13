class Figure:

    def __init__(self, name):
        self.name = name


    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area() + figure.area()
        else:
            raise ValueError('Wrong class was given')