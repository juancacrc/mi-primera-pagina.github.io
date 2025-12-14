espacios = 0
tortuga = 't'

def adelante(pasos_adelante):
    global espacios
    for i in range(pasos_adelante):
        print(' ' * espacios + tortuga)
        espacios += 1


def abajo(pasos_abajo):
    global espacios
    for i in range(pasos_abajo):
        print(' ' * espacios + tortuga)


# Programa principal
escalones = int(input("¿Cuántos escalones desea dibujar? "))

for i in range(escalones):
    pasos_adelante = int(input("\nPasos hacia adelante: "))
    adelante(pasos_adelante)

    pasos_abajo = int(input("Pasos hacia abajo: "))
    abajo(pasos_abajo)

print("\nFin del dibujo 🐢")
