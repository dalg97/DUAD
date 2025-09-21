def reverse_string(word):
    new_word = ""
    for letter in range(len(word),0,-1):
        new_word += word[letter-1]    
    print(new_word)

reverse_string("hola soy Diego")
