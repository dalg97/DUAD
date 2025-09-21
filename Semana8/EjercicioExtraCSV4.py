import csv 

def get_file(path):
    classif = input("Ingrese el Desarrollador: ")
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        print(f"Juegos Desarrollados por {classif}:\n")
        for row in reader:
            if not row:
                continue
            elif row[2] == classif:
                print(f"- {row[0]} (Clasificacion: {row[3]}, Genero: {row[1]})")
                    

get_file("games.csv")