import random


archivo = open("C:/Users/hp/Desktop/Proyectos_Personales-VC/Aristaas.csv", "w")
archivo.write("Source;Target;Weight\n")

relaciones = {} 

for i in range(3000):
    source = random.randint(0, 1499)
    target = random.randint(0, 1499)
    weight = random.randint(1, 3)

    if (source, target) in relaciones:
        weight = relaciones[(source, target)]
    else:
        relaciones[(source, target)] = weight

    archivo.write(str(source) + ";" + str(target)+ ";" + str(weight) + "\n")

archivo.close()
