from .searcher import Searcher
from typing import Dict
import itertools

class CommonSearcher(Searcher):
    params: Dict
    param_indices: Dict
    started: bool

    def __init__(self, params: Dict):
        self.params = params        
        self.perms = itertools.product(*params.values())
        
    def __iter__(self) -> Searcher:
        return self               