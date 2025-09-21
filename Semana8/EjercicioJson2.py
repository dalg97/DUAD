import json

def get_file(path):
    with open(path, 'r') as f:
        data = json.load(f)
    print(json.dumps(data,indent=4))
    add_pokemon(data)
    print(json.dumps(data,indent=4))



def add_pokemon(data):
    pokemon_primary = {}
    pokemon_secondary = {}
    base = {}
    type_list = []
    name = input("Nombre: ")
    type_p = input("Tipo: ") 
    hp = int(input("HP: "))
    attack = int(input("Ataque: "))
    defense = int(input("Defensa: "))
    sp_attack = int(input("SP Attack: "))
    sp_defense = int(input("SP Defensa: "))
    speed = int(input("Speed: "))
    type_list.append(type_p)
    base['HP'] = hp
    base['Attack'] = attack
    base['Defense'] = defense
    base['SP. Attack'] = sp_attack
    base['SP. Defense'] = sp_defense
    base['Speed'] = sp_attack
    pokemon_secondary['english'] = name
    pokemon_primary['name'] = pokemon_secondary
    pokemon_primary['type'] = type_list
    pokemon_primary['base'] = base
    data.append(pokemon_primary)
    save_file(data)

def save_file(data):
    json_str = json.dumps(data, indent=4)
    with open("pokemons.json", "w") as f:
        f.write(json_str)

get_file("pokemons.json")
