from .repeatabletfm import RepeatableTfm
from .taggeddataframe import TaggedDataFrame
from .coltag import ColTag
from typing import List
from scipy.special import boxcox1p
from scipy import stats
import pandas as pd

# SkewTfm skews all the given columns using box cox.
class SkewTfm(RepeatableTfm):
    def __init__(self, cols: List[str], lam:float=0.15, max_skewness:float=0.75):
        self.cols = cols
        self.max_skewness = max_skewness
        self.lam = lam

    def operate(self, df: TaggedDataFrame) -> None:
        for name in self.cols:
            if stats.skew(df.frame[name].dropna()) > self.max_skewness:
                df.frame[name] = boxcox1p(df.frame[name], self.lam)
                df.tag_column(name, ColTag.modified)

