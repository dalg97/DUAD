def create_file(path):
	with open(path,'a') as file:
		file.write("Hello\nWorld\nThis\nis\nPython\n")

def get_words(path):
	create_file(path)
	with open(path,'r') as file:
		for line in file.readlines():
			append_words('new_word.txt',line)

def append_words(path,word):
	with open(path,'a') as file:
		file.write(word.strip() + " ")
		
get_words('words.txt')