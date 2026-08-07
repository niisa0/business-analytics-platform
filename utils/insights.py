def generate_business_insights(df):
    if df.empty:
        return []

    top_region = (
        df.groupby("Region")["Revenue"]
        .sum()
        .idxmax()
    )

    top_region_revenue = (
        df.groupby("Region")["Revenue"]
        .sum()
        .max()
    )

    top_category = (
        df.groupby("Category")["Profit"]
        .sum()
        .idxmax()
    )

    top_category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .max()
    )

    top_product = (
        df.groupby("Product")["Profit"]
        .sum()
        .idxmax()
    )

    top_product_profit = (
        df.groupby("Product")["Profit"]
        .sum()
        .max()
    )

    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()

    profit_margin = (
        (total_profit / total_revenue) * 100
        if total_revenue > 0
        else 0
    )

    return [
        f"{top_region} is the top-performing region with ${top_region_revenue:,.2f} in revenue.",
        f"{top_category} is the most profitable category with ${top_category_profit:,.2f} in profit.",
        f"{top_product} is the most profitable product with ${top_product_profit:,.2f} in profit.",
        f"Overall profit margin is {profit_margin:.1f}%."
    ]