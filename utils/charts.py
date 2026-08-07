import plotly.express as px


def revenue_profit_trend(df):
    monthly_data = (
        df.groupby(df["Order_Date"].dt.to_period("M"))
        [["Revenue", "Profit"]]
        .sum()
        .reset_index()
    )

    monthly_data["Order_Date"] = (
        monthly_data["Order_Date"]
        .astype(str)
    )

    fig = px.line(
        monthly_data,
        x="Order_Date",
        y=["Revenue", "Profit"],
        markers=True,
        title="Revenue and Profit Over Time",
        labels={
            "Order_Date": "Month",
            "value": "Amount ($)",
            "variable": "Metric"
        },
        color_discrete_map={
            "Revenue": "#2E90C9",
            "Profit": "#56F8A7"
        }     
    )

    fig.update_layout(
        xaxis_tickangle=0,
        legend_title_text="Metric"
    )

    return fig


def category_performance_chart(df):
    category_data = (
        df.groupby("Category")[["Revenue", "Profit"]]
        .sum()
        .reset_index()
        .sort_values("Revenue", ascending=True)
    )

    fig = px.bar(
        category_data,
        x=["Profit", "Revenue"],
        y="Category",
        orientation="h",
        barmode="group",
        title="Category Performance",
        labels={
            "value": "Amount ($)",
            "variable": "Metric",
            "Category": "Category"
        },
        color_discrete_map={
            "Revenue": "#2E90C9",
            "Profit": "#56F8A7"
        }     
    )

    fig.update_layout(
        legend_title_text="Metric",
        legend_traceorder="reversed"
    )

    return fig


def regional_performance_chart(df):
    region_data = (
        df.groupby("Region")[["Revenue", "Profit"]]
        .sum()
        .reset_index()
        .sort_values("Revenue", ascending=True)
    )

    fig = px.bar(
        region_data,
        x=["Profit", "Revenue"],
        y="Region",
        orientation="h",
        barmode="group",
        title="Regional Performance",
        labels={
            "value": "Amount ($)",
            "variable": "Metric",
            "Region": "Region"
        },
        color_discrete_map={
            "Revenue": "#2E90C9",
            "Profit": "#56F8A7"
        }     
    )

    fig.update_layout(
        legend_title_text="Metric",
        legend_traceorder="reversed"
    )

    return fig


def top_products_chart(df, top_n=10):
    product_data = (
        df.groupby("Product")[["Revenue", "Profit"]]
        .sum()
        .reset_index()
        .sort_values("Revenue", ascending=True)
        .tail(top_n)

    )

    fig = px.bar(
        product_data,
        x="Revenue",
        y="Product",
        orientation="h",
        title=f"Top {top_n} Products by Revenue",
        labels={
            "Revenue": "Revenue ($)",
            "Product": "Product"
        }
    )

    fig.update_traces(
        marker_color="#2E90C9"
    )

    return fig


def revenue_vs_profit_chart(df):
    product_data = (
        df.groupby("Product")[["Revenue", "Profit"]]
        .sum()
        .reset_index()
    )

    fig = px.scatter(
        product_data,
        x="Revenue",
        y="Profit",
        hover_name="Product",
        title="Revenue vs Profit by Product",
        labels={
            "Revenue": "Revenue ($)",
            "Profit": "Profit ($)"
        }
    )

    fig.update_traces(
        marker=dict(
            size=12,
            color="#2E90C9"
        )
    )

    return fig