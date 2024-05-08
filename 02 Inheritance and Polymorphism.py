class Shape:
    def no_of_sides(self):
        pass

    def three_dimensional(self):
        print('I am 3D from Shape class')

class Rectangle:
    def no_of_sides(self):
        print('I have 4 sides. I am from Rectangle class')

class Polygon:
    def no_of_sides(self):
        print('I have 3 sides. I am from Polygon class')

# Create object from Rectangle class
re = Rectangle()

# Override the no_of_sides of parent class
re.no_of_sides()

# Create object from Polygon class
poly = Polygon()
poly.no_of_sides()