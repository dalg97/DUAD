import csv 

def get_file(path):
    classif = input("Ingrese la Clasificacion: ")
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        print(f"Juegos con clasificación {classif}:\n")
        for row in reader:
            if not row:
                continue
            elif row[3] == classif:
                for x, y in zip(headers, row):
                    print(f"{x}: {y}")
                print(" ")

get_file("games.csv")