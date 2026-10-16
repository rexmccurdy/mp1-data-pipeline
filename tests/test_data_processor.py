#tests/test_data_processor.py

import pandas as pd
import pytest

from src.data_processor import handle_missing, remove_duplicates, remove_outliers


def test_remove_duplicates(sample_df):

    sample_df = remove_duplicates(sample_df)
    assert len(sample_df) == 98

    # TODO: Call remove_duplicates() on sample_df.
    # TODO: Assert that 98 rows remain.


def test_handle_missing_rows(sample_df):
    # Arrange: use the existing rating column.
    df = sample_df[["rating"]].copy()
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce") 

    df = handle_missing(df, "rows")
    assert len(df) == 97
    # note: errors="coerce" converts invalid numeric strings to missing values.

    # TODO: Call handle_missing() with axis="rows".
    # TODO: Assert that 97 rows remain.
    


def test_remove_outliers_iqr(sample_df):
    # Arrange: use numeric ratings and exclude missing values.
    df = sample_df[["rating"]].copy()
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce") 
    df = df.dropna()
    # note: errors="coerce" converts invalid numeric strings to missing values.
    df = remove_outliers(df, ["rating"], "iqr", 1.5)
    assert len(df) == 95
    # TODO: Call remove_outliers() for ["rating"], using method="iqr", and threshold=1.5.
    # TODO: Assert that 95 rows remain.
    

# TODO: Use test_remove_outliers_iqr() as a reference to write test_remove_outliers_zscore(). Use the same numeric rating data without missing values, but set method="zscore" and threshold=3. Check the expected result for zscore and update your assertions accordingly.

# TODO: Use test_validate_dataframe_with_missing_column() as a reference to write test_remove_outliers_with_unsupported_method(). Use pytest.raises(ValueError) to confirm that remove_outliers() raises an error when called with method="unknown".

def test_remove_outliers_zscore(sample_df):
    df = sample_df[["rating"]].copy()
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce") 
    df = df.dropna()

    df = remove_outliers(df, ["rating"], "zscore", 3)
    print(len(df))
    assert len(df) == 95


def test_validate_dataframe_with_unsupported_method(sample_df):
    df = sample_df[["rating"]].copy()
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce") 
    df = df.dropna()

    with pytest.raises(ValueError):
        remove_outliers(df, ["rating"], "unknown", 5)
        
