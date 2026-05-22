import pandas as pd

def load_data():
    return pd.read_csv("data/titanic.csv")

def clean_data(df):
    """
    Cleans the input DataFrame by dropping rows where all values are missing
    and converting categorical columns to lowercase.
    """
    df = df.dropna(how="all") 
    categorical_cols = df.select_dtypes(include="object").columns
    df[categorical_cols] = df[categorical_cols].apply(lambda col: col.str.lower())
    return df