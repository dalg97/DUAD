list_to_remove = ["last_name","favorite_food"]
dict1 = {
    "first_name": "Diego",
    "last_name": "Lopez",
    "age": 27,
    "role": "System Engineer",
    "favorite_food" : "pizza" 
}
for key in list_to_remove:
    dict1.pop(key)
print(dict1)