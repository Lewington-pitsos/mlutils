import pandas as pd

# for every column in the dataframe with at least 1 bad value
# another column is created with 1's for all entities with
# bad values in the original column.
def add_bad_indicator_vars(df: pd.DataFrame):
    df.apply(process_col, args=(df,))

def process_col(col: pd.Series, df: pd.DataFrame):
    pass
    if col.isna().any():
        bad_col_name = col.name + "_is_bad"
        assert(bad_col_name not in df)
