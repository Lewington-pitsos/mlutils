from .searcher import Searcher
from typing import Dict, List, Type
from .xgbtypes import ParamDict, IntDict

class GridSearcher(Searcher):
    def __init__(self, params: ParamDict):
        self.params = params        
        self.paramIndices = {}

        for param in params:
            self.paramIndices[param] = 0
        

    def __iter__(self) -> Type[Searcher]:
        return self


    def __next__(self) -> IntDict:
        if self.param_step():
            return self.current_params()
        else:
            raise StopIteration
        

    def param_step(self) -> bool:
        updated = False
        for param in self.paramIndices:
            if self.untried_values_for(param):
                self.paramIndices[param] += 1
                updated = True
                break
        
        return updated
            
    def current_params(self) -> IntDict:
        current_params = {}
        for param, index in self.paramIndices.items():
            current_params[param] = self.params[param][index]
        
        return current_params

    def untried_values_for(self, param: str):
        return self.paramIndices[param] < len(self.params[param]) - 1