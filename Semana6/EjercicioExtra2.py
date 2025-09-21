
def word_list(my_list,num):
    new_list = []
    for word in my_list:
        if len(word) > num:
            new_list.append(word)
    return new_list

final_list = word_list(["hola","carroceria","sal","viento","mundo"],5)
print(final_list)