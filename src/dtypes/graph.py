import heapq
from typing import Union
from collections import defaultdict
from .person_node import PersonNode
from .node_edge import NodeEdge


class Graph:
    def __init__(self):
        self.connections = defaultdict[int, list[tuple[int, int]]](list)
        self.nodes = dict[int, PersonNode]()

    def add_node(self, node: PersonNode):
        self.nodes[node.id] = node

    def add_edge(self, edge: NodeEdge):
        self.connections[edge.source].append((edge.target, edge.weight))
        self.connections[edge.target].append((edge.source, edge.weight))

    def kruskal(self):
        edges = list[tuple[int, int, int]]()
        for u in self.connections:
            for v, weight in self.connections[u]:
                edges.append((weight, u, v))

        edges.sort()

        parent = {node: node for node in self.connections}
        rank = {node: 0 for node in self.connections}
        minimum_spanning_tree = list[tuple[int, int, int]]()

        def find(node: int):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1: int, node2: int):
            root1 = find(node1)
            root2 = find(node2)
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1] += 1

        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                minimum_spanning_tree.append((u, v, weight))

        return minimum_spanning_tree

    def dijkstra(self, source: int, destination: int):
        distances = {node: float("inf") for node in self.connections}
        distances[source] = 0
        previous: dict[int, Union[int, None]] = {
            node: None for node in self.connections
        }
        pq: list[tuple[int, int]] = [(0, source)]

        while pq:
            dist, node = heapq.heappop(pq)

            if dist > distances[node]:
                continue

            for neighbor, weight in self.connections[node]:
                if dist + weight < distances[neighbor]:
                    distances[neighbor] = dist + weight
                    previous[neighbor] = node
                    heapq.heappush(pq, (dist + weight, neighbor))

        path = list[int]()
        current_node = destination
        while current_node is not None:
            path.insert(0, current_node)
            current_node = previous[current_node]

        return path
