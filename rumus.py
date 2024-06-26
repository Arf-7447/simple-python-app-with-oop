import math

class Shape:
    def volume(self):
        pass

class Cylinder(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class RectangularPrism(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3

class Cone(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * math.pi * self.radius ** 2 * self.height
