name = input("Enter your name: ")
lastname = input("Enter your lastname: ")
age = int(input("Enter your age: "))

if age > 0 and age <= 3:
    print(f"{name} {lastname} es un bebe")
elif age > 3 and age < 9:
    print(f"{name} {lastname} es un nino")
elif age >= 9 and age <= 13:
    print(f"{name} {lastname} es un preadolescente")
elif age > 13 and age < 18:
    print(f"{name} {lastname} es un adolescente")
elif age >= 18 and age < 30:
    print(f"{name} {lastname} es un adulto joven")
elif age >= 30 and age < 60:
    print(f"{name} {lastname} es un adulto")
elif age >= 60:
    print(f"{name} {lastname} es un adulto mayor")
else:
    print("Edad invalida")