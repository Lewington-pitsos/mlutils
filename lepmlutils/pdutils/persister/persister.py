import pandas as pd
from typing import Set


class Persister():
    def __init__(self, data_path: str):
        self.data_path: str = data_path
        self.sets: Set[str] = set()

    def save(self, name: str, df: pd.DataFrame):
        if name in self.sets:
            raise KeyError(f"name {name} is already saved, cannot overwrite implicitly")

        self.sets.add(name)
