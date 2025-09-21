the_list = [4,8,1,45,-6,1,0]
counter = 0
for num in the_list:
    if num <= 0:
        counter += 1
if counter > 0:        
    print("Hay al menos un numero negativo o cero")
else:
    print("Todos los numeros son positivos")    