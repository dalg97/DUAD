def convertir_a_entero(list):
    print("Resultado: ")
    for index in list:
        try:
          new_int = int(index)
          print(f"'{index}' se ha convertido a {new_int}" )
        except ValueError:
          print(f"No se pudo convertir el elemento {index}")


def main():
  try:
    my_list = ['hola','2','5.5','comida','15']
    convertir_a_entero(my_list)
  except Exception as ex:
    print(ex)

if __name__ == '__main__':
    main()


