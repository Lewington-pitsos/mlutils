from .transform import Transform
from .taggeddataframe import TaggedDataFrame
from pandas import DataFrame

class LepDataFrame():
    def __init__(self, df: DataFrame):
        self.tagged_df = TaggedDataFrame(df)
        self.frame = df
    
    def apply(self, tfm: Transform):
        tfm.operate(self.tagged_df)