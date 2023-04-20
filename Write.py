import csv

dades = [
    ['x:','y:', 'z:','temps:'],
    ['x:','y:', 'z:','temps:'],
    ['x:','y:', 'z:','temps:'],
]

with open('archivo.csv','w',newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(dades)