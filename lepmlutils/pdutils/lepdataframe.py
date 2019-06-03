from __future__ import annotations
from .transform import Transform
from .taggeddataframe import TaggedDataFrame
from pandas import DataFrame
from typing import List

class LepDataFrame():
    def __init__(self, df: DataFrame):
        self.tagged_df = TaggedDataFrame(df)
        self.applied: List[Transform] = []
    
    def apply(self, tfm: Transform) -> None:
        tfm.operate(self.tagged_df)
        self.applied.append(tfm)

    def frame(self) -> DataFrame:
        return self.tagged_df.frame
    
    def copy_from(self, df: 'LepDataFrame') -> None:
        for tfm in df.applied:
            self.reapply(tfm)
    
    def reapply(self, tfm: Transform) -> None:
        tfm.re_operate(self.tagged_df)
        self.applied.append(tfm)
    
    def apply_sequence(self, seq: List[Transform]) -> None:
        for tfm in seq:
            self.apply(tfm)