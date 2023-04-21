import csv

def read():
    with open('archivo.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
