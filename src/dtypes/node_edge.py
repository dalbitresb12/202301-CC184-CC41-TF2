from csv import DictReader
from util.io import from_datapath


class NodeEdge:
    def __init__(self, source: int, target: int, weight: int):
        self.source = source
        self.target = target
        self.weight = weight

    def to_string(self) -> str:
        return f"{self.source},{self.target},{self.weight}"

    def to_mapping(self) -> dict[str, str]:
        content = dict[str, str]()
        content["Source"] = str(self.source)
        content["Target"] = str(self.target)
        content["Weight"] = str(self.weight)
        return content

    @classmethod
    def from_csv(cls, filename: str, use_datapath: bool = True):
        if use_datapath:
            filename = from_datapath(filename)
        connections = list[cls]()
        with open(filename, "r", encoding="utf-8") as file:
            reader = DictReader(file, delimiter=",")
            for row in reader:
                source = int(row["Source"])
                target = int(row["Target"])
                weight = int(row["Weight"])
                connections.append(cls(source, target, weight))
        return connections
