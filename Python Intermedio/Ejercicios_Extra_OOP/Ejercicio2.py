class Animal:
    def __init__ (self,name):
        self.name = name
    def speak(self):
        return "Make some sound"
class Dog(Animal):
    def speak(self):
        return "Guau"
class Cat(Animal):
    def speak(self):
        return "Miau"
    
dog_1 = Dog("Loki")
cat_1 = Cat("Coco")
print(f"{dog_1.name} says {dog_1.speak()}")
print(f"{cat_1.name} says {cat_1.speak()}")

