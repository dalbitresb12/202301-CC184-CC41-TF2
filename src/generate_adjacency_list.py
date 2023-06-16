#!/usr/bin/env python3

from csv import DictWriter
from dtypes import NodeEdge
from util.io import from_datapath
from collections import defaultdict


def generate_adjacency_list(connections: list[NodeEdge]):
    adjacency_list = defaultdict[int, list[int]](list)
    for conn in connections:
        adjacency_list[conn.source].append(conn.target)
        adjacency_list[conn.target].append(conn.source)
    return adjacency_list


def main():
    connections = NodeEdge.from_csv("connections.csv")
    adjacency_list = generate_adjacency_list(connections)
    sorted_sources = sorted(adjacency_list.keys())
    with open(
        from_datapath("adjacency_list.csv"), "w", encoding="utf-8", newline=""
    ) as file:
        writer = DictWriter(file, ["Source", "Target"])
        writer.writeheader()
        for source in sorted_sources:
            target = " ".join([str(x) for x in adjacency_list[source]])
            writer.writerow({"Source": source, "Target": target})


if __name__ == "__main__":
    main()
