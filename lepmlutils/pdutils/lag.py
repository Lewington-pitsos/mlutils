from .help import *
from .internal import *
from typing import List
import pandas as pd

hash_col = "--HASHCOL--"
lagged_time_col = "--LAGGEDTIMECOL--"
lagged_hash_col = "--LAGGEDHASHCOL--"

def create_lag(
    df, 
    target: str, 
    time_col: str, 
    lag: int, 
    group_cols: List[str]=[],
) -> None: 
    joined_name = "-".join(group_cols)
    lag_feat_name = f"{target}-{joined_name}-{time_col}Lag{lag}"
    for col in [hash_col, lagged_time_col, lagged_hash_col, lag_feat_name]:
        assert not contains(df, col)
    assert df[time_col].dtype == "int"

    df[hash_col] = multi_concat_feat(df, group_cols + [time_col])
    df[lagged_time_col] = df[time_col] + lag
    df[lagged_hash_col] = multi_concat_feat(df, group_cols + [lagged_time_col])

    assert already_grouped(df, hash_col, target)

    df[lag_feat_name] = df[hash_col].map(
        map_from(df, lagged_hash_col, target),
    )

    df.drop([hash_col, lagged_time_col, lagged_hash_col], axis=1, inplace=True)

def already_grouped(df, group_col: str, target: str) -> bool:
    groups = df.groupby(group_col).agg({target: ["min", "max"]})
    return groups[(target, "min")].equals(groups[(target, "max")])

def create_grouped_lag(
    df, 
    target: str, 
    time_col: str, 
    lag: int, 
    group_cols: List[str]=[],
) -> None: 
    pass