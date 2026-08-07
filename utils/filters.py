def apply_filters(
    df,
    start_date,
    end_date,
    selected_regions,
    selected_categories,
    selected_segments
):
    filtered_df = df.copy()

    filtered_df = filtered_df[
        (filtered_df["Order_Date"].dt.date >= start_date)
        & (filtered_df["Order_Date"].dt.date <= end_date)
    ]

    if selected_regions:
        filtered_df = filtered_df[
            filtered_df["Region"].isin(selected_regions)
        ]

    if selected_categories:
        filtered_df = filtered_df[
            filtered_df["Category"].isin(selected_categories)
        ]

    if selected_segments:
        filtered_df = filtered_df[
            filtered_df["Customer_Segment"].isin(selected_segments)
        ]

    return filtered_df