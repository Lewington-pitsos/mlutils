from .transform import Transform
from .taggeddataframe import TaggedDataFrame
from .coltag import ColTag
from typing import List
import pandas as pd

# DropTfm removes a number of columns from a dataframe.
class DropTfm(Transform):
    def __init__(self, to_drop: List[str]):
        self.to_drop = to_drop
    
    def operate(self, df: TaggedDataFrame) -> None:
        # df.frame.apply(self.process_bad_value_cols, args=(df,))
        pass
        
    # Alias for operate.
    def re_operate(self, new_df: TaggedDataFrame) -> None:
        self.operate(new_df)

