from typing import Dict, List

class Recorder():
    records: List[Dict]

    def __init__(self):
        self.records = []
    
    def sort_records(self):
        self.records = sorted(self.records, key = lambda i: i["test_score"], reverse=True)
    
    def best_n_params(self, records_wanted: int) -> List[Dict]:
        self.pre_process()
        return self.records[:records_wanted]

    def best_params(self) -> Dict:
        self.pre_process()
        return self.records[0]
    
    def pre_process(self):
        self.confirm_records()
        self.sort_records()

    def confirm_records(self):
        if (len(self.records) == 0):
            raise RuntimeError("Attempt to access tuning results before tuning has occurred")