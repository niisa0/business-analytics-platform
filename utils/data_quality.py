import pandas as pd


def get_data_quality_summary(raw_df, cleaned_df):
    parsed_dates = pd.to_datetime(
        raw_df["Order_Date"],
        errors="coerce"
    )

    summary = {
        "original_rows": len(raw_df),
        "cleaned_rows": len(cleaned_df),
        "duplicates_removed": raw_df.duplicated().sum(),
        "invalid_dates_removed": parsed_dates.isna().sum(),
        "missing_unit_price": raw_df["Unit_Price"].isna().sum(),
        "missing_unit_cost": raw_df["Unit_Cost"].isna().sum(),
        "missing_region": raw_df["Region"].isna().sum(),
        "missing_customer_segment": raw_df["Customer_Segment"].isna().sum(),
    }

    return summary