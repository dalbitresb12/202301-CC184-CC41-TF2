#!/usr/bin/env python3

from csv import DictWriter
from dtypes import PersonNode
from util.io import list_from_txt, from_datapath
from random import randint, choice


def generate_nodes(size: int) -> list[PersonNode]:
    # get names list
    sample_names = list_from_txt("name_list.txt")
    # get faculty names list
    sample_faculties = list_from_txt("faculty_list.txt")
    # generate nodes
    nodes = list[PersonNode]()
    for id in range(size):
        name = choice(sample_names)
        edad = randint(18, 30)
        faculty = choice(sample_faculties)
        nodes.append(PersonNode(id + 1, name, edad, faculty))
    return nodes


def main():
    nodes = generate_nodes(1500)
    with open(from_datapath("nodes.csv"), "w", encoding="utf-8", newline="") as file:
        writer = DictWriter(file, ["ID", "Name", "Age", "Faculty"])
        writer.writeheader()
        writer.writerows([node.to_mapping() for node in nodes])


if __name__ == "__main__":
    main()
