word = input("Ingrese la palabra: ")
charact = input("Ingrese el caracter a buscar: ")
def character(word,charact):
    count = 0
    for letter in word:
        if letter == charact:
            count += 1
    return count

amount_of_times = character(word,charact)
print(f"Se ha encontrado {amount_of_times} veces el caracter en el texto {word}")