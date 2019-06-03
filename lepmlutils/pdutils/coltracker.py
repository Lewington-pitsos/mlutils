from typing import Dict, List
from .coltag import ColTag
from pandas import DataFrame

# ColTracker knows all the column names of a DataFrame and which
# tags each has been given. It can return a list of column names
# based on given tags.
class ColTracker():
    def __init__(self, df: DataFrame):
        self.tags: Dict[str, List[ColTag]] = {}
        for name in df.columns.values:
            self.tags[name] = [ColTag.original]

    def get_all(self, tag: ColTag) -> List[str]:
        col_names: List[str] = []

        for name, tags in self.tags.items():
            if tag in tags:
                col_names.append(name)

        return col_names
    
    def tag(self, name: str, tag: ColTag) -> None:
        self.tags[name].append(tag)