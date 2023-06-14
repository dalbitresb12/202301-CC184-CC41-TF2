#!/usr/bin/env python3

from util.nodes import ConnectionsDict
from util.file_handlers import from_datapath
from random import randint


def generate_connections(size: int) -> ConnectionsDict:
    connections = dict[tuple[int, int], int]()
    while len(connections) != size:
        source = randint(1, 1500)
        target = randint(1, 1500)
        if (source, target) in connections:
            continue
        weight = randint(1, 3)
        connections[(source, target)] = weight
    return connections


def main():
    connections = generate_connections(3000)
    content = "\n".join(
        [
            f"{source},{target},{connections[(source, target)]}"
            for source, target in connections
        ]
    )
    with open(from_datapath("connections.csv"), "w", encoding="utf-8") as file:
        file.write("Source,Target,Weight\n")
        file.write(content)


if __name__ == "__main__":
    main()
