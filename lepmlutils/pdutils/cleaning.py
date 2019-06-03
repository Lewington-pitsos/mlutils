import pandas as pd
import numpy as np
from pandas.api.types import is_string_dtype

def categorize(df :pd.DataFrame):
        for col_name in df.select_dtypes(include="object").columns.values:
                mapping_col_name = col_name + "_mapping" 
                assert(mapping_col_name not in df)
                df[col_name] = df[col_name].astype('category')
                df[mapping_col_name] = df[col_name].cat.codes

# def remove_bad_vals_basic(df: pd.DataFrame):
#         add_bad_indicator_vars(df)
#         replace_bad_values_with_median(df)
#         categorize(df)
