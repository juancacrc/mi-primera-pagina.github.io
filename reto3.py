

tortuga = 'T'
espacios = 0

# Avanzar hacia adelante (derecha)
pasos_adelante = int(input("¿Cuántos pasos hacia adelante? "))

for i in range(pasos_adelante):
    print(" " * espacios + tortuga)
    espacios += 1

# Bajar (hacia abajo)
pasos_abajo = int(input("¿Cuántos pasos hacia abajo? "))

for i in range(pasos_abajo):
    print(" " * espacios + tortuga)
