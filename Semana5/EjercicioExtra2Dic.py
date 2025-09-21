employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

departments = {}
for employee in employees:
    names = {}
    people = []
    department_name = employee.get("department")
    names["name"] = employee.get("name")
    names["email"] = employee.get("email")
    if departments.get(department_name):
        departments[department_name].append(names)
    else:
        people.append(names)
        departments[department_name] = people
print(departments)