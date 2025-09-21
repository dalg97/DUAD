name = input("Ingrese el nombre del hotel: ")
stars_number = int(input("Ingrese el numero de estrellas del hotel: "))
amount_of_rooms = int(input("Ingrese la cantidad de habitaciones del hotel: "))#To add multiples rooms
counter = 1
hotel = {
    "nombre": name,
    "numero_de_estrellas": stars_number,
    "habitaciones": []
}
while counter <= amount_of_rooms:
    rooms = {}
    room_number = int(input("Ingrese el numero de habitacion: "))
    rooms["numero"] = room_number
    floor_number = int(input("Ingrese el numero de piso: "))
    rooms["piso"] = floor_number
    room_night_price = int(input("Ingrese el precio por noche: "))
    rooms["precio_por_noche"] = room_night_price
    hotel["habitaciones"].append(rooms)
    counter += 1
print(hotel)