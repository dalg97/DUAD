def vocals(word):
    count = 0
    vocal_list = ["a","e","i","o","u"]
    for letter in word:
        for vocal in vocal_list:
            if letter == vocal:
                count += 1
                break
    return count

amount_of_vocals = vocals("Comiendo")
print(f"Hay {amount_of_vocals} vocales")
