from main import Rectangle, Square, Circle
rect_1 = Rectangle(3,4,50,100)

square_1 = Square(5,5,40)

circle_1 = Circle(2,6,70)

figures = [rect_1, square_1, circle_1]
for figure in figures:
    print(figure.__class__.__name__, figure)