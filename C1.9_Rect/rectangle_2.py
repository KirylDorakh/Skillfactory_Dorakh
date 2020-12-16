from rectangle1 import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
square_1 = Square(4)
square_2 = Square(10)
circle_1 = Circle(2)
circle_2 = Circle(5)


print("area_rect_1", rect_1.getArea())
print("area_rect_2", rect_2.getArea(), )
print("area_square_1", square_1.getAreaSquare())
print("area_square_2", square_2.getAreaSquare())
print("area_circle_1", circle_1.getAreaCircle())
print("area_circle_2", circle_2.getAreaCircle())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print('Square')
        print(figure.getAreaSquare())
    elif isinstance(figure, Circle):
        print('Circle')
        print(figure.getAreaCircle())
    else:
        print('Rectangle')
        print(figure.getArea())