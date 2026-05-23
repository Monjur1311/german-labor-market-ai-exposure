"""Utility functions for thesis notebooks."""

import pandas as pd


def add_post_variables(df, year_col="year", exposure_col="ai_exposure", post_year=2023):
    """Add post indicator and continuous DiD interaction."""
    df = df.copy()
    df["post"] = (df[year_col] >= post_year).astype(int)
    df["ai_post"] = df[exposure_col] * df["post"]
    return df
