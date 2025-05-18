import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Take A path as argument
    Read the data as pandas dataFrame
    Return the data
    """
    try:
        loaded_data = pd.read_csv(path)
        return loaded_data
    except Exception:
        print("Exception error: couldn't load data file")
        exit(1)
