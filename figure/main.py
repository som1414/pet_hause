class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square(Rectangle):

    def __init__(self, a):
        Rectangle.__init__(self, a, b=a)
        # self.a = a
        # self.b = a

class Circle(Square):

    def get_area(self):
        return 3.14 * Rectangle.get_area(self)