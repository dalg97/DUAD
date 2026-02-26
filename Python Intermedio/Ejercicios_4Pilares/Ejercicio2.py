from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self,radio):
        area = math.pi * (radio ** 2)
        return area
    
    def calculate_perimeter(self,radio):
        perimeter = 2 * math.pi * radio
        return perimeter
    
class Square(Shape):
    def calculate_area(self,side):
        area = side ** 2
        return area
    
    def calculate_perimeter(self,side):
        perimeter = 4 * side
        return perimeter
    
class Rectangle(Shape):
    def calculate_area(self,base, height):
        area = base * height
        return area
    
    def calculate_perimeter(self,length,width):
        perimeter = 2 * (length + width)
        return perimeter

circle1 = Circle()
print(f"The area of the circle is: {circle1.calculate_area(4)} and the perimeter is: {circle1.calculate_perimeter(4)}")

square1 = Square()
print(f"The are of the square is: {square1.calculate_area(3)} and the perimeter is: {square1.calculate_perimeter(3)}")

rectangle1 = Rectangle()
print(f"The area of the rectangle is: {rectangle1.calculate_area(6,2)} and the perimeter is: {rectangle1.calculate_perimeter(3,5)}")