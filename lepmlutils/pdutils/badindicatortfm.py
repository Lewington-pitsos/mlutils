from .transform import Transform
from .lepdataframe import LepDataFrame
from .coltag import ColTag
from typing import List
import pandas as pd

# BadIndicatorTfm adds a new indicator column (indicating a 
# bad value) to the given data frame for each existing 
# column which contains at least one bad value.
class BadIndicatorTfm(Transform):
    def __init__(self):
        self.altered: List[str] = []
    
    def operate(self, df: LepDataFrame) -> None:
        df.df.apply(self.process_bad_value_cols, args=(df,))

    def process_bad_value_cols(self, col: pd.Series, df: LepDataFrame) -> None:
        if col.isna().any():
            self.create_indicator(col, df)
            
            # for use in re_opeate
            self.altered.append(col.name)
    
    def create_indicator(self, col: pd.Series, df: LepDataFrame) -> None:
        bad_col_name = col.name + "_is_bad"
        assert(bad_col_name not in df.df)

        df.df[bad_col_name] = 0
        df.df.loc[df.df[col.name].isna(), bad_col_name] = 1
        
        # update tags
        df.tag_column(col.name, ColTag.modified)
        df.tag_column(bad_col_name, ColTag.bad_indicator)
    
    # re_operate adds indicator columns for bad values to the new dataframe
    # for every column that contained a bad value on the first operation.
    def re_operate(self, old_df: LepDataFrame, new_df: LepDataFrame) -> None:
        new_df.df.apply(self.process_old_cols, args=(new_df))

    def process_old_cols(self, col: pd.Series, df: LepDataFrame) -> None:
        for name in self.altered:
            self.create_indicator(df.df[name], df)

