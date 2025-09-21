def create_file(path):
	with open(path,'a') as file:
		file.write("hello i am diego and this is python\n")
		file.write("i am a system engineer")
	
def get_words(path):
	create_file(path)
	with open(path,'r') as file:
		for line in file.readlines():
			append_words('upper.txt',line.upper())

def append_words(path,word):
	with open(path,'a') as file:
		file.write(word)
		
get_words('lower.txt')
