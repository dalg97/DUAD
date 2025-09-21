import json

def get_file(path):
    with open(path, 'r') as f:
        data = json.load(f)
    get_pokemon_type(data)

def get_pokemon_type(data):
    pokemon_type = input("Ingrese el tipo de pokemon (Fire, Water,Normal,Electric): ")
    for dictionary in data:
        if dictionary["type"][0] == pokemon_type:
            print(f"{dictionary["name"]["english"]}")
        

get_file("pokemons.json")