import pandas as pd
from typing import Set


class Persister():
    def __init__(self, data_path: str):
        self.data_path: str = data_path
        self.sets: Set[str] = set()

    def save(self, name: str, df: pd.DataFrame):
        if name in self.sets:
            raise KeyError(f"name {name} is already saved, cannot overwrite implicitly")

        df.to_csv(self.path_for(name), index=False)

        self.sets.add(name)

    def overwrite(self, name: str, df: pd.DataFrame):
        if name not in self.sets:
            raise KeyError(f"name {name} is not already saved, cannot overwrite.")

        df.to_csv(self.path_for(name), index=False)

        self.sets.add(name)

    def path_for(self, name:str) ->str:
        return self.data_path + "/" + name + ".csv"

    def load(self, name:str) -> pd.DataFrame:
        if name not in self.sets:
            raise KeyError(f"name {name} does not match any existing saves")

        return pd.read_csv(self.path_for(name))
