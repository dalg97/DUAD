class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
try:
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    if width < 0 or height < 0:
        raise ValueError()
    rectangle_1 = Rectangle(width, height) 
    print(rectangle_1.get_area())
    print(rectangle_1.get_perimeter())
except ValueError:
    print("Width and height must be non-negative integers")


