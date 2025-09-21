#Accesar variable  dentro  de una funcion
def scope1():
    color = "black"
    return color
color = scope1()
print(color)

#Accesar variable global
num = 8
def change_number():
    global num
    num = 5 
    return num
print(change_number())
print(num)



