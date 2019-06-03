from .coltracker import ColTracker
from pandas import DataFrame

class LepDataFrame(ColTracker):
    def __init__(self, df: DataFrame):
        super().__init__(df)
        self.df: DataFrame = df
    
    @property
    def _constructor(self):
        return LepDataFrame