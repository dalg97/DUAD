class Vehicle:
    def __init__(self,brand,year):
        self._brand = brand
        self._year = year

    def get_info(self):
        pass


class Car(Vehicle):
    def __init__(self,brand,year,door,type):
        super().__init__(brand,year)
        self.door = door
        self.type = type


    def get_info(self):
        return f"Brand: {self._brand}\nYear: {self._year}\nDoors: {self.door}\nType: {self.type}"
    

class Motorcycle(Vehicle):
    def __init__(self,brand,year,color):
        super().__init__(brand,year)
        self.color = color
    
    def get_info(self):
        return f"Brand: {self._brand}\nYear: {self._year}\nColor: {self.color}"
    
car1 = Car("Toyota",2015,4,"4x4")
motorcycle1 = Motorcycle("Yamaha",2011,"blue")
print(car1.get_info())
print("")
print(motorcycle1.get_info())