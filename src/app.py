#!/usr/bin/env python3

from dtypes import Graph, NodeEdge, PersonNode


def main():
    graph = Graph()

    nodes = PersonNode.from_csv("nodes.csv")
    for node in nodes:
        graph.add_node(node)

    connections = NodeEdge.from_csv("connections.csv")
    for conn in connections:
        graph.add_edge(conn)

    source = int(input("Estudiante de inicio: "))
    target = int(input("Estudiante de destino: "))

    if source not in graph.connections or target not in graph.connections:
        print("No hay relación entre estos nodos.")
    else:
        shortest_path = graph.dijkstra(source, target)
        print(
            f"La conexión más corta desde el estudiante {source} hasta el estudiante {target} es: {shortest_path}"
        )
        print("Atributos de los nodos intermedios:")
        for node_id in shortest_path:
            print("ID del nodo:", node_id)
            if node_id in graph.nodes:
                node = graph.nodes[node_id]
                print(f"Atributos del nodo: {node.to_string()}")
            else:
                print(f"El nodo {node_id} no tiene atributos asociados.")


if __name__ == "__main__":
    main()
