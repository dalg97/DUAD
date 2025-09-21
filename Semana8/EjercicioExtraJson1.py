import json

def get_file(path):
    with open(path, 'r') as f:
        data = json.load(f)
    for dictionary in data:
        print(f"Nombre: {dictionary["name"]["english"]}\nTipo: {dictionary["type"][0]}")
        for power,number in dictionary["base"].items():
            print(f"{power}: {number}")
        print("")

get_file("pokemons.json")
