import csv

with open('archivo.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print("X:{0}, Y:{1}, Z:{2}, TEMPS:{3}".format(row[0],row[1],row[2],row[3]))
