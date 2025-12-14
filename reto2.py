# recrear movimiento de la tortuga hacia abajo


tortuga = 't'
espacios = 0

pasos = int (input("¿Cuántos pasos debe avanzar la tortuga hacia abajo? "))

for i in range(pasos):
    espacios += 1
    print(" " * espacios + tortuga)
