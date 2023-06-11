import random
import time

# nombres aleatorios
nombres = []
with open('Nombre.csv', 'r') as hoja:
    for line in hoja:
        nombres.append(line.strip())

# facultad aleatoria
facultad = ["Administracion en Hotelería y Turismo", "Arquitectura", "Artes Contemporáneas", "Ciencias de la Salud",
            "Ciencias Humanas", "Comunicaciones", "Derecho", "Diseño", "Economía", "Educación", "Ingeniería",
            "Negocios", "Psicología"]

with open("Nodos.csv", "w") as archivo:
    archivo.write("ID;Nombre;Edad;Facultad\n")
    for i in range(1500):
        seleccionador = random.randint(0, len(nombres) - 1)
        edad = 17 + random.randint(0, 14)
        selec = random.randint(0, len(facultad) - 1)
        archivo.write(f"{i};{nombres[seleccionador]};{edad};{facultad[selec]}\n")

