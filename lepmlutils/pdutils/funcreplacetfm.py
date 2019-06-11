from .transform import Transform
from .taggeddataframe import TaggedDataFrame
from .coltag import ColTag
from typing import Dict, List
import pandas as pd

# FuncReplaceTfm takes a callback and replaces every bad
# value in the given columns with the output of that 
# callback. 
class FuncReplaceTfm(Transform):
    def __init__(self, callback):
        self.callback = callback

    def operate(self, df: TaggedDataFrame, cols: List[str], data_df: pd.DataFrame=None) -> None:
        self.cols = cols
        if data_df is None:
            self.data_df = df.frame.copy(deep=True)
        else:
            self.data_df = data_df.frame.copy(deep=True)

        self.fill_bad_vals(df)

    def fill_bad_vals(self, df: TaggedDataFrame):
        for name in self.cols:
            df.frame[name] = df.frame[name].fillna(
                self.callback(
                    name,
                    self.data_df
                )
            )
            df.tag_column(name, ColTag.modified)
    
    # re_operate fills the original columns with the 
    # values given by the callback, passing in the 
    # original data df.
    def re_operate(self, new_df: TaggedDataFrame) -> None:
        self.fill_bad_vals(new_df)

