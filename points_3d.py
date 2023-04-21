import numpy as np
import random as random
import time as time
#Numpy info: https://www.digitalocean.com/community/tutorials/vectors-in-python
#Random info: https://www.w3schools.com/python/module_random.asp

#PARAMETRES
punt_inici = np.array([0,0,0])
pas_maxim = 20
pasos = 4
periode = 2              #en segons

#PARAMETRES_2
hora_inici = time.time()
posicio_actual_temporal = [0,0,0,0]
pasos = 4

#TEMPS INICI
t_inici = time.time()

def direccio():
    sentit = [-1,1]
    return np.array([
        random.random()*random.choice(sentit),
        random.random()*random.choice(sentit),
        random.random()*random.choice(sentit),
        ])

def fer_pas_Atemporal(posicio_actual, pas_maxim):
    pas = posicio_actual + direccio() * pas_maxim
    return pas

def fer_pas_temporal(posicio_actual_temporal, hora_inici, pas_maxim): #Llista x,y,z,hora_del_punt
    punt_anterior = np.array([
        posicio_actual_temporal[0],
        posicio_actual_temporal[1],
        posicio_actual_temporal[2]
    ])
    punt = fer_pas_Atemporal(punt_anterior, pas_maxim)
    hora_actual = time.time()
    beeing = punt.tolist()
    beeing.append(hora_actual - hora_inici)
    return beeing

    

def generar_infinit(punt,pasos,pas_maxim,t_inici,periode):
    punt = fer_pas_Atemporal(punt, pas_maxim)
    t_actual = time.time()
    beeing = punt.tolist()
    beeing.append(t_actual - t_inici)
    print(beeing)
    while True:
        punt = fer_pas_Atemporal(punt, pas_maxim)
        t_actual = time.time()
        beeing = punt.tolist()
        beeing.append(t_actual - t_inici)
        print(beeing)
        if periode != 0:
            time.sleep(periode)

def llista_punts(punt,pasos,pas_maxim,t_inici,periode):
    punt = fer_pas_Atemporal(punt, pas_maxim)
    t_actual = time.time()
    beeing = punt.tolist()
    beeing.append(t_actual - t_inici)
    print(beeing)
    for i in range(pasos):
        punt = fer_pas_Atemporal(punt, pas_maxim)
        t_actual = time.time()
        beeing = punt.tolist()
        beeing.append(t_actual - t_inici)
        print(beeing)
        if periode != 0:
            time.sleep(periode)

if __name__ == "__main__":
    #llista_punts(punt_inici,pasos,pas_maxim,t_inici,periode)
    #generar_infinit(punt_inici,pasos,pas_maxim,t_inici,periode)
    punt = posicio_actual_temporal
    for i in range(pasos):
        punt = fer_pas_temporal(punt, hora_inici, pas_maxim)
        print(punt)