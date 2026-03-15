class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @property
    def salary(self):
        return self.__salary
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
        
    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("Salary is negative")
        self.__salary = value

    def promote(self, percentage):
        if percentage < 0:
            raise ValueError("El porcentaje no puede ser negativo")
        self.__salary += self.__salary * (percentage / 100)


empleado1 = Employee("Diego",2000)
print(f"{empleado1.name} y {empleado1.salary}")
empleado1.promote(20)
print(f"{empleado1.name} y {empleado1.salary}")