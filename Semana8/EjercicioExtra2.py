def create_file(path):
	with open(path,'a') as file:
		file.write("Hello\nI am\nDiego and\nthis is\nPython\n")

def get_words(path):
	count = 0
	create_file(path)
	with open(path) as file:
		for line in file.readlines():
			words_list = line.split()
			count += len(words_list)
	print(f"The file contains {count} words")
		
get_words('amount_of_words.txt')