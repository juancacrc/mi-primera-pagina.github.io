
adelante = ('n')
abajo = ('n')

def adelante(pasos_adelante):

    print ('' * pasos_adelante)
    global espacios
    espacios = espacios + pasos_adelante
    camino_abajo = espacios + '|\n'
    print('t', end='')

def abajo(pasos_abajo):
    global espacios
    for i in range (pasos_abajo -1):
        camino_abajo = '' * espacios + '|\n'
        print(camino_abajo, end= '')
        print('' * espacios + 't')
