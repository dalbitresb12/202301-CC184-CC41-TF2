#!/usr/bin/env python3

from csv import DictWriter
from dtypes import NodeEdge
from util.io import from_datapath
from random import randint


def generate_connections(size: int) -> list[NodeEdge]:
    connections = dict[tuple[int, int], NodeEdge]()
    while len(connections) != size:
        source = randint(1, 1500)
        target = randint(1, 1500)
        if (source, target) in connections:
            continue
        weight = randint(1, 3)
        connections[(source, target)] = NodeEdge(source, target, weight)
    return [item for _, item in connections.items()]


def main():
    connections = generate_connections(3000)
    with open(
        from_datapath("connections.csv"), "w", encoding="utf-8", newline=""
    ) as file:
        writer = DictWriter(file, ["Source", "Target", "Weight"])
        writer.writeheader()
        writer.writerows([conn.to_mapping() for conn in connections])


if __name__ == "__main__":
    main()
