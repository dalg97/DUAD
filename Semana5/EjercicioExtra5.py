new_list = []
for counter in range(5):
    word = input(f"Ingrese la palabra{counter+1}: ")
    if len(word) > 4:
        new_list.append(word)
print(new_list)