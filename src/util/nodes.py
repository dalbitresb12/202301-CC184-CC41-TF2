from util.file_handlers import from_datapath
from collections import defaultdict
from typing import TypeAlias


ConnectionsDict: TypeAlias = dict[tuple[int, int], int]
AdjacencyListDict: TypeAlias = defaultdict[int, list[int]]


def parse_connections(filename: str) -> ConnectionsDict:
    connections: ConnectionsDict = dict()
    with open(from_datapath(filename), "r", encoding="utf-8") as file:
        for line in file:
            parts = [int(part) for part in line.strip().split(",")]
            connections[(parts[0], parts[1])] = parts[2]
    return connections


class PersonNode:
    def __init__(self, id: int, name: str, age: int, faculty: str) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.faculty = faculty

    def to_string(self) -> str:
        return f"{self.id},{self.name},{self.age},{self.faculty}"

    @classmethod
    def from_string(cls, input: str):
        parts = input.split(",")
        return cls(int(parts[0]), parts[1], int(parts[2]), parts[3])
