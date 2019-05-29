from typing import Dict, List
from pandas import DataFrame
from .recorder import Recorder
from .partition import Partition
from .settuner import SetTuner

class Tuner(Recorder):

    tuner: SetTuner

    def __init__(self):
        self.tuner = SetTuner()
        super().__init__()
    
    def tune(
        self, 
        search_params: Dict,
        set_params: Dict, 
        dataset: DataFrame ,
        features: List[str],
        targets: List[str],
        folds: int,
    ) -> List[Dict]:
        folds = Partition(dataset, folds)

        for split in folds:
            fold_records = self.tuner.tune(
                search_params,
                set_params,
                split["train"][features],
                split["train"][targets],
                split["test"][features],
                split["test"][targets]
            )

            self.records.append(*fold_records)

        self.sort_records()
        return self.records 