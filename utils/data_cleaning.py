import pandas as pd

def clean_data(df):
    df = df.copy()

    df = df.drop_duplicates()

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"],
        errors="coerce"
    )

    df["Unit_Price"] = pd.to_numeric(
        df["Unit_Price"],
        errors="coerce"
    )

    df["Unit_Cost"] = pd.to_numeric(
        df["Unit_Cost"],
        errors="coerce"
    )

    df["Unit_Price"] = df["Unit_Price"].fillna(
        df.groupby("Product")["Unit_Price"].transform("median")
    )

    df["Unit_Cost"] = df["Unit_Cost"].fillna(
        df.groupby("Product")["Unit_Cost"].transform("median")
    )

    df["Region"] = df["Region"].fillna("Unknown")

    df["Customer_Segment"] = df["Customer_Segment"].fillna("Unknown")

    df = df.dropna(subset=["Order_Date"])

    return df