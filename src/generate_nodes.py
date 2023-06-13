#!/usr/bin/env python3

from util.file_handlers import list_from_txt, from_datapath
from util.nodes import PersonNode
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
    content = "\n".join([node.to_string() for node in nodes])
    with open(from_datapath("nodes.csv"), "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    main()
