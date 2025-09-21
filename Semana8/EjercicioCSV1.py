import csv

games = int(input("Cuantos juegos deseas agregar: "))
counter = 1

games_list = []
while counter <= games:
    
    name = input("Nombre: ")
    gender = input("Genero: ")
    develop = input("Desarrollador: ")
    classif = input("Clasificacion: ")

    game_dict = {
    'Nombre': name,
	'Genero': gender,
	'Desarrollador': develop,
	'Clasificacion_ESRB': classif
    }
    games_list.append(game_dict)
    counter += 1

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

write_csv_file('games.csv', games_list, games_list[0].keys())

