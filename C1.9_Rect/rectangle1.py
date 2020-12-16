class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        return self.a * self.b

class Square:
    def __init__(self,a):
        self.a = a
    def getAreaSquare(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r
    def getAreaCircle(self):
        return (self.r**2)*3.14