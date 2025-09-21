def create_file(path):
	with open(path,'a') as file:
		file.write("Numb\nIn the End\nPapercut\nNew Divide\n")

def get_songs(path):
	create_file(path)
	temp_list = []
	with open(path,'r') as file:
		for line in file.readlines():
			temp_list.append(line.strip())
	temp_list.sort()
	for song in temp_list:
		append_songs('new_songs.txt',f"{song}\n")

def append_songs(path,song):
	with open(path,'a') as file:
		file.write(song)
		
get_songs('songs.txt')