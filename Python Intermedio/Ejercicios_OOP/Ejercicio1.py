import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area_result = math.pi * (self.radius ** 2)
        return area_result


circle = Circle(5)
print(circle.get_area())