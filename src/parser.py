import csv

with open('../data/week1/players.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    count = 0
    for row in reader:
        print(row.get('age'))
        if count == 2:
            break
        count += 1