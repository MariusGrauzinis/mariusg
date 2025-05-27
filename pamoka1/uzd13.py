class Shape:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def area(self):
        return 0  


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle", 4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height 


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.name = "Square"  

print(Square(4).area())
print(Rectangle(3, 5).area())