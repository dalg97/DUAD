import csv 

def get_file(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
        games = {}
        for row in reader:
            if not row:
                continue
            if games.get(row[1]):
                games[row[1]] = games.get(row[1]) + 1
            else:    
                games[row[1]] = 1
        for header,count in games.items():
            print(f"{header}: {count}")

get_file("games.csv")