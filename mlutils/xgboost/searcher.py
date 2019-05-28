from abc import ABCMeta, abstractmethod
from typing import Type
from .xgbtypes import IntDict

class Searcher(metaclass=ABCMeta):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self) -> IntDict:
        pass