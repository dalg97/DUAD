import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_result = math.pi * (self.radius ** 2)
        print(f"The area is {area_result}")


circle = Circle(5)
circle.area()