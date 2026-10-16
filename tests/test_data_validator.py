import pytest
from src import validate_dataframe

def test_validate_dataframe_removes_invalid_ratings(sample_df):
    required = ["record_id", "name", "rating", "category", "status"]
    numeric = ["rating"]
    out = validate_dataframe(sample_df, required_columns=required, numeric_columns=numeric)

    assert len(out) == 98
    assert out.columns.tolist() == required
    # TODO: Set the required and numeric column names.
    # TODO: Call validate_dataframe().
    # TODO: Assert that 98 rows remain and all five columns are preserved.
    

def test_validate_dataframe_with_missing_column(sample_df):
    required = ["record_id", "name", "rating", "category", "status", "nonexistent"]
    numeric = ["rating"]
    with pytest.raises(ValueError):
        validate_dataframe(sample_df, required_columns=required, numeric_columns=numeric)
    # TODO: Set required_columns to include a nonexistent column.
    # TODO: Use pytest.raises(ValueError) around validate_dataframe().
    