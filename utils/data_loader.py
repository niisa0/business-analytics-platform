import pandas as pd


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Data file not found: {file_path}"
        )

    except pd.errors.EmptyDataError:
        raise ValueError(
            "The data file is empty."
        )

    except pd.errors.ParserError:
        raise ValueError(
            "The data file could not be parsed correctly."
        )