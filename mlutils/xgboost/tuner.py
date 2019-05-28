from xgboost import XGBClassifier
from typing import Dict
from .xgbtypes import ParamDict, IntDict
from .gridsearcher import GridSearcher

class Tuner():
    def __init__(
        self, 
        search_params: ParamDict,
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
    
    def tune(self):
        params = self.param_searcher)
        classifier = XGBClassifier(
            **self.set_params,
            
        )

