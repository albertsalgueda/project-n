import points_3d as points
import Write as wr
import time as time
import Read as rd

#PARAMETRES_2
hora_inici = time.time()
posicio_actual_temporal = [0,0,0,0]
pasos = 4
pas_maxim = 20
interval = 1

#TEMPS INICI
t_inici = time.time()

def main():
    punt = posicio_actual_temporal
    for i in range(pasos):
        punt = points.fer_pas_temporal(punt, hora_inici, pas_maxim)
        wr.functiondades(punt)
        time.sleep(interval)

def main_infinite():
    punt = posicio_actual_temporal
    while True:
        punt = points.fer_pas_temporal(punt, hora_inici, pas_maxim)
        wr.functiondades(punt)
        time.sleep(interval)


if __name__ == "__main__":
    #main()
    main_infinite()