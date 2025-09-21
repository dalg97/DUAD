products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
total = {}
for dictionary in products:
    category = dictionary.get("category")
    price = dictionary.get("price") 
    if total.get(category):
        total[category] += price
    else:
        total[category] = price               
print(total)


                                                                                                                                                                                    