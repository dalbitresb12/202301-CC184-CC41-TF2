from typing import Union
from os.path import exists

__cached_data_files_path__: Union[str, None] = None


def from_datapath(filepath: str, stop_at_repo: bool = True) -> str:
    global __cached_data_files_path__

    def __recursive_finder__(path: str) -> str:
        if exists(f"{path}/data"):
            return path
        if stop_at_repo and exists(f"{path}/.git"):
            raise RuntimeError("Unable to find data path")
        return __recursive_finder__(f"../{path}")

    if __cached_data_files_path__ is None:
        __cached_data_files_path__ = __recursive_finder__(".")
    return f"{__cached_data_files_path__}/data/{filepath}"


def list_from_txt(filename: str, use_datapath: bool = True) -> list[str]:
    if use_datapath:
        filename = from_datapath(filename)
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]
