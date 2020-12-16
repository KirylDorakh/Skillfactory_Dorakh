class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def rectArea(self):
        return self.width * self.height

    def infoRect(self):
        return f"Info about {__class__.__name__}: x = {self.x}, y = {self.y}, " \
               f"width = {self.width}, height = {self.height}, Area = {self.rectArea()}"


