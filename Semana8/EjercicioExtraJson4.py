import json

def get_file(path):
    with open(path, 'r') as f:
        data = json.load(f)
    group_pokemon(data)


def group_pokemon(data):
    pokemon = {}
    average = 0
    result = 0
    for dictionary in data:
        if pokemon.get(dictionary['type'][0]):
            result = average_cal(dictionary["base"])
            pokemon[dictionary["type"][0]] += result
        else:
            result = average_cal(dictionary["base"])
            pokemon[dictionary["type"][0]] = result
    for type_pokemon,value in pokemon.items():
        print(f"Tipo: {type_pokemon} -> Promedio de nivel: {round(value,2)}")

def average_cal(base):
    count = 0
    result = 0
    for x,y in base.items():
        count = count + y
    result = count / len(base)
    return result

get_file("pokemons.json")
