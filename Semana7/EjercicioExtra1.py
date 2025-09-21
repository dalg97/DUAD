def user_data():
	name = input("Ingrese su nombre: ")
	if name.isdigit():
		raise ValueError("El nombre no puede ser un numero")

	try:
		age = int(input("Ingrese su edad: "))
		print(f"Hola {name}, su edad es {age}")	
	except ValueError as ex:
		print("Numero no valido")

def main():
	try:
		user_data()
	except Exception as ex:
		print(ex)   


if __name__ == '__main__':
    main()