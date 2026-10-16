#tests/test_data_output.py

import pandas as pd

from src import save_data


def test_save_data_creates_csv(sample_df, tmp_path):
    output_path = tmp_path / "clean.csv"

    filepath = save_data(sample_df, output_path)

    assert filepath == output_path

    output_df = pd.read_csv(filepath)

    assert output_df.shape == sample_df.shape

    # TODO: Call save_data() and store its return value.
    # TODO: Assert that the returned path is correct.
    # TODO: Read the saved CSV with pandas.
    # TODO: Assert that its row count and column names match sample_df.
    
