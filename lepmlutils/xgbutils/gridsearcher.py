from .commonsearcher import CommonSearcher
from typing import Dict

class GridSearcher(CommonSearcher):
    def __init__(self, params: Dict):
        super().__init__(params)       
        
    def __next__(self) -> Dict:
        current_params = {}
        values = next(self.perms)
        for index, key in enumerate(self.params.keys()):
            current_params[key] = values[index] 

        return current_params                  