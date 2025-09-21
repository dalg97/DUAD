def sumar_valores(list):
    result = 0
    for index in list:
        try:
          new_float = float(index)
          print(f"{index} sumado correctamente" )
          result += new_float
        except ValueError:
          print(f"Elemento invalido: {index}")
    print(f"Total de la suma: {result}")

def main():
  try:
    my_list = ['hola','2','5.5','comida','7.3','prueba','4']
    sumar_valores(my_list)
  except Exception as ex:
    print("teat")

if __name__ == '__main__':
    main()


