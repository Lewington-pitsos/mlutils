import pandas as pd
from typing import List

class MergedDataFrame(pd.DataFrame):
    _metadata = ["train_indices", "test_indices", "train_targets"]

    def __init__(self, *args, **kw):
        super(MergedDataFrame, self).__init__(*args, **kw)

    @property
    def _constructor(self):
        return MergedDataFrame
    
    def trainFrame(self) -> pd.DataFrame:
        return self[self[self.index_col].isin(self.train_indices)]

def merged_df(traindf: pd.DataFrame, testdf: pd.DataFrame, targets: List[str], index_col: str) -> MergedDataFrame:
        n_train = traindf.shape[0]
        
        all_data = pd.concat((traindf, testdf), sort=False).reset_index(drop=True)

        df = MergedDataFrame(all_data)
        print(all_data[index_col].values[0])
        df.train_indices = all_data[index_col].values[:n_train]
        df.test_indices = all_data[index_col].values[n_train:]
        df.index_col = index_col
        return df
