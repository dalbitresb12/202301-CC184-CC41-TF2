import pandas as pd

archivo = open("C:/Users/hp/Desktop/Proyectos_Personales-VC/ListaAdyacencia.csv", "w")
archivo.write("Source;Target\n")

aristas_df = pd.read_csv(r"C:\Users\hp\Desktop\Proyectos_Personales-VC\Aristaas.csv", delimiter=";", encoding="Latin-1")

lista_adyacencia = {}

for _, row in aristas_df.iterrows():
    source = row["Source"]
    target = row["Target"]

    if source in lista_adyacencia:
        lista_adyacencia[source].append(target)
    else:
        lista_adyacencia[source] = [target]

    if target in lista_adyacencia:
        lista_adyacencia[target].append(source)
    else:
        lista_adyacencia[target] = [source]

etiquetas_nodos_ordenadas = sorted(set(lista_adyacencia.keys()), key=int)

for nodo in etiquetas_nodos_ordenadas:
    conexiones = lista_adyacencia.get(nodo, [])
    conexiones_str = ", ".join(map(str, conexiones))
    archivo.write(f"{nodo}; {conexiones_str}\n")

archivo.close()
