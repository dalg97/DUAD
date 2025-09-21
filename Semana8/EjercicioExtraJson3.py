import json

def get_file(path):
    with open(path, 'r') as f:
        data = json.load(f)
    for dictionary in data:
        print(f"Nombre: {dictionary["name"]["english"]}\n"
        f"Ataque: {dictionary["base"]["Attack"]}\n"
        f"Defensa: {dictionary["base"]["Defense"]}\n"
        f"Velocidad: {dictionary["base"]["Speed"]}\n")

get_file("pokemons.json")
