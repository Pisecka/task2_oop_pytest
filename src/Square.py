from src.Figure import Figure


class Square(Figure):
    def __init__(self, name, a):
        super().__init__(name)
        self.a = a

    def area(self):
        return self.a ** 2





    
s1 = Square('square', 7)