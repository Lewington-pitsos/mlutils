from __future__ import annotations
from abc import ABCMeta, abstractmethod
from .lepdataframe import LepDataFrame


# Transform represents an operation that can be performed on and
# alters a LepDataFrame in place.
class Transform():
    @abstractmethod
    def operate(self, df: LepDataFrame) -> None:
        pass
    
    def reoperate(self, old_df: LepDataFrame, df: LepDataFrame) -> None:
        pass