text = input("Ingrese una linea de texto: ")
def append_words(path,txt):
	with open(path,'a') as file:
		file.write("\n"+txt)
		
append_words('append.txt',text)