from .help import *
import pandas as pd
from typing import List


class Imputer():
    def __init__(
        self, 
        df: pd.DataFrame, 
        true_nas: List[str],
        int_ord_cats: List[str],
        int_unord_cats: List[str],
        str_ord_cats: List[str],
        str_unord_cats: List[str]
    ): 
        str_dups = set(str_ord_cats) - set(str_unord_cats)
        assert len(str_dups) == 0, f"string columns {str_dups} are duplicated"

        int_dups = set(int_ord_cats) - set(int_unord_cats)
        assert len(int_dups) == 0, f"integer columns {int_dups} are duplicated"

        all_str_cats = str_ord_cats + str_unord_cats

        assert set(all_str_cats) == set(str_cols(df)), "all string columns from the data frame should have been passed in as string categoricals"
        
         

        pass
