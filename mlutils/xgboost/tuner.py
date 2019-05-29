from xgboost import XGBClassifier
from typing import Dict, List, Type
from .gridsearcher import GridSearcher
from .searcher import Searcher

class Tuner():
    param_searcher: Searcher
    set_params: Dict
    records: List[Dict]

    def __init__(
        self, 
        search_params: Dict,
        set_params: Dict, 
        train_features, 
        train_targets,
        test_features,
        test_targets
    ):
        self.param_searcher = GridSearcher(search_params)
        self.set_params = set_params
        self.train_features = train_features 
        self.train_targets = train_targets
        self.test_features = test_features
        self.test_targets = test_targets
        self.records = []
    
    def tune(self) -> List[Dict]:    
        for candidates in self.param_searcher:
            args: Dict = {**self.set_params, **candidates}
            classifier = XGBClassifier(args)
            classifier.fir(self.train_features, self.train_targets)
            score: float = classifier(self.test_features, self.test_targets)
            self.save_score(candidates, score)
        self.sort_records()
        return self.records

    def save_score(self, params_used: Dict, score: float):
        self.records.append({
            "score": score,
            "params": params_used
        })
    
    def sort_records(self):
        self.records = sorted(self.records, key = lambda i: i["score"], reverse=True)
    
    def best_n_params(self, records_wanted: int) -> List[Dict]:
        return self.records[:records_wanted]

    def best_params(self) -> Dict:
        return self.records[0]
