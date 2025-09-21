first_list = ["first_name","last_name","role","favorite_color","favorite_sport"]
second_list = ["Diego","Lopez","System Engineer","blue","soccer"]
dict1 = {}
for index in range(0,len(first_list)):
    dict1[first_list[index]] = second_list[index]
print(dict1)
