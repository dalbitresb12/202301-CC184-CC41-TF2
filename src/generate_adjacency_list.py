from util.file_handlers import from_datapath
from util.nodes import ConnectionsDict, AdjacencyListDict, parse_connections
from collections import defaultdict


def generate_adjacency_list(connections: ConnectionsDict) -> AdjacencyListDict:
    adjacency_list: AdjacencyListDict = defaultdict(list)
    for source, target in connections:
        adjacency_list[source].append(target)
        adjacency_list[target].append(source)
    return adjacency_list


def main():
    connections = parse_connections("connections.csv")
    adjacency_list = generate_adjacency_list(connections)
    sorted_keys = sorted(adjacency_list.keys())
    content = "\n".join(
        [
            f"{key},{' '.join([str(x) for x in adjacency_list[key]])}"
            for key in sorted_keys
        ]
    )
    with open(from_datapath("adjacency_list.csv"), "w", encoding="utf-8") as file:
        file.write("Source,Target\n")
        file.write(content)


if __name__ == "__main__":
    main()
