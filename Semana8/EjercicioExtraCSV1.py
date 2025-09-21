import csv 

def get_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            for x, y in zip(headers, row):
                print(f"{x}: {y}")
            print(" ")

get_file("games.csv")