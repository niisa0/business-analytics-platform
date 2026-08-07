def add_business_metrics(df):
    df = df.copy()

    df["Revenue"] = df["Quantity"] * df["Unit_Price"]
    df["Cost"] = df["Quantity"] * df["Unit_Cost"]
    df["Profit"] = df["Revenue"] - df["Cost"]

    df["Profit_Margin"] = (
        df["Profit"] / df["Revenue"]
    ) * 100

    return df


def calculate_kpis(df):
    if df.empty:
        return {
            "total_revenue": 0,
            "total_profit": 0,
            "total_orders": 0,
            "average_order_value": 0,
            "profit_margin": 0,
        }

    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order_ID"].nunique()

    average_order_value = (
        total_revenue / total_orders
        if total_orders > 0
        else 0
    )

    profit_margin = (
        (total_profit / total_revenue) * 100
        if total_revenue > 0
        else 0
    )

    return {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "average_order_value": average_order_value,
        "profit_margin": profit_margin,
    }