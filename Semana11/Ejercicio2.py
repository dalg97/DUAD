class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Bus:
    max_passengers = 3
    main_bus = []
    def add_passenger(self, current_passenger):
        if len(self.main_bus) < self.max_passengers:
            self.main_bus.append(current_passenger)
            print("Passenger added")
        else:
            print("Bus is full")

    def remove_passenger(self):
        if self.main_bus:
            for index in range(len(self.main_bus)):
                passenger = self.main_bus.pop(0)
                print(f"Passenger {passenger.name} removed")
        else:
            print("Bus is empty")

    def show_passengers(self):
        for passenger in self.main_bus:
            print(f"Name: {passenger.name}")  

person_1 = Persona("Diego", 30)
person_2 = Persona("Ana", 25)
person_3 = Persona("Luis", 28)
person_4 = Persona("Maria", 22)


bus_1 = Bus()
bus_1.add_passenger(person_1)
bus_1.add_passenger(person_2)
bus_1.add_passenger(person_3)
bus_1.add_passenger(person_4)  

bus_1.show_passengers()

bus_1.remove_passenger()
bus_1.add_passenger(person_4)
bus_1.show_passengers()