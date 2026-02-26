class Person:
    def __init__(self,name):
        self.name  = name

class Worker:
    def __init__(self,salary):
        self.salary = salary

class Role:
    def __init__(self,role_name):
        self.role_name = role_name

class New_Hire(Person,Worker,Role):
    def __init__(self, name,salary,role_name):
        Person.__init__(self,name)
        Worker.__init__(self,salary)
        Role.__init__(self,role_name)
    
    def accepted(self):
        print(f"The application by {self.name} was accepted\nSalary: {self.salary}\nRole: {self.role_name}")

new_hire1 = New_Hire("Luis",800000,"Engineer")
new_hire1.accepted()
