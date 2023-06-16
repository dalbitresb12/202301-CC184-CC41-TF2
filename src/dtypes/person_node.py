from csv import DictReader
from util.io import from_datapath


class PersonNode:
    def __init__(self, id: int, name: str, age: int, faculty: str) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.faculty = faculty

    def to_string(self) -> str:
        return f"{self.id},{self.name},{self.age},{self.faculty}"
    
    def to_mapping(self) -> dict[str, str]:
        content = dict[str, str]()
        content["ID"] = str(self.id)
        content["Name"] = self.name
        content["Age"] = str(self.age)
        content["Faculty"] = self.faculty
        return content

    @classmethod
    def from_csv(cls, filename: str, use_datapath: bool = True):
        if use_datapath:
            filename = from_datapath(filename)
        nodes = list[cls]()
        with open(filename, "r", encoding="utf-8") as file:
            reader = DictReader(file, delimiter=",")
            for row in reader:
                id = int(row["ID"])
                name = row["Name"]
                age = int(row["Age"])
                faculty = row["Faculty"]
                nodes.append(cls(id, name, age, faculty))
        return nodes
