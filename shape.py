
PI=3.1416

print(PI)

def my_func():
    pass

class Shape:

    color = "blue"

    def __init__(self, name):
        self.name = name
        self.area = 0
    
    def get_area(self):
        raise NotImplementedError()

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color      

class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.name=name
        self.length=length
        self.width=width

    def get_area(self):
        self.area=self.length*self.width
        return self.area

class Square(Rectangle):
    def __init__(self, name, side):
        self.name=name
        self.side=side

    def get_area(self):
        self.area=self.side*self.side
        return self.area    

class SquareWithAHoleInside(Square):
    def __init__(self, name, side, hole_size):
        self.name=name
        self.side=side
        self.hole_size=hole_size

    def get_area(self):
        self.area=super().get_area()-self.hole_size
        return self.area


class Circle(Shape):

    MY_PI=3.14

    def __init__(self, name, radius):
        self.name=name
        self.radius=radius
        self.color = "red"

    def get_area(self):
        self.area = PI*self.radius*self.radius
        return self.area



