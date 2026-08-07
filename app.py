import streamlit as st
from utils.data_loader import load_data
from utils.data_cleaning import clean_data
from utils.analytics import (
    add_business_metrics,
    calculate_kpis
    )
from utils.charts import (
    revenue_profit_trend,
    category_performance_chart,
    regional_performance_chart,
    top_products_chart,
    revenue_vs_profit_chart
)
from utils.filters import apply_filters
from utils.insights import generate_business_insights
from  utils.data_quality import get_data_quality_summary
from utils.report_generator import(
    generate_csv_report,
    generate_excel_report
)


st.set_page_config(
    page_title="Business Analytics Platform",
    page_icon="📊",
    layout="wide"
)

try:
    raw_df = load_data("data/sales_data.csv")

    df = clean_data(raw_df)
    df = add_business_metrics(df)

    quality = get_data_quality_summary(raw_df, df)

except (FileNotFoundError, ValueError) as error:
    st.error(str(error))
    st.stop()

st.sidebar.header("Filters")

st.sidebar.caption(
    "Filters update all KPIs, charts, insights, and exported reports."
)

start_date = st.sidebar.date_input(
    "Start Date",
    value=df["Order_Date"].min().date(),
    min_value=df["Order_Date"].min().date(),
    max_value=df["Order_Date"].max().date()
)

end_date = st.sidebar.date_input(
    "End Date",
    value=df["Order_Date"].max().date(),
    min_value=df["Order_Date"].min().date(),
    max_value=df["Order_Date"].max().date()
)

selected_regions = st.sidebar.multiselect(
    "Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

selected_categories = st.sidebar.multiselect(
    "Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

selected_segments = st.sidebar.multiselect(
    "Customer Segment",
    options=sorted(df["Customer_Segment"].unique()),
    default=sorted(df["Customer_Segment"].unique())
)

if start_date > end_date:
    st.error("Start Date cannot be later than End Date.")
    st.stop()

filtered_df = apply_filters(
    df,
    start_date,
    end_date,
    selected_regions,
    selected_categories,
    selected_segments
)

current_filter_state = (
    start_date,
    end_date,
    tuple(selected_regions),
    tuple(selected_categories),
    tuple(selected_segments)
)

if filtered_df.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

kpis = calculate_kpis(filtered_df)

st.title("Business Analytics & Reporting Platform")

st.caption(
    "Interactive analysis of revenue, profitability, products, regions, and business performance."
)

st.subheader("Executive Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Revenue",
    f"${kpis['total_revenue']:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${kpis['total_profit']:,.2f}"
)

col3.metric(
    "Total Orders",
    f"{kpis['total_orders']:,}"
)

col4, col5 = st.columns(2)

col4.metric(
    "Average Order Value",
    f"${kpis['average_order_value']:,.2f}"
)

col5.metric(
    "Profit Margin",
    f"{kpis['profit_margin']:.1f}%"
)

st.subheader("Performance Trends")

trend_chart = revenue_profit_trend(filtered_df)

st.plotly_chart(
    trend_chart,
    use_container_width=True
)

st.subheader("Performance Breakdown")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        category_performance_chart(filtered_df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        regional_performance_chart(filtered_df),
        use_container_width=True
    )

st.subheader("Product Analysis")

st.plotly_chart(
    top_products_chart(filtered_df),
    use_container_width=True
)

st.plotly_chart(
    revenue_vs_profit_chart(filtered_df),
    use_container_width=True
)

insights = generate_business_insights(filtered_df)

st.subheader("Business Insights")

for insight in insights:
    st.info(insight)

with st.expander("Data Quality Summary"):
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Original Rows",
        f"{quality['original_rows']:,}"
    )

    col2.metric(
        "Cleaned Rows",
        f"{quality['cleaned_rows']:,}"
    )

    col3.metric(
        "Duplicates Removed",
        f"{quality['duplicates_removed']:,}"
    )

    col4.metric(
        "Invalid Dates Removed",
        f"{quality['invalid_dates_removed']:,}"
    )

    col5, col6, col7, col8 = st.columns(4)

    col5.metric(
        "Unit Price Filled",
        f"{quality['missing_unit_price']:,}"
    )

    col6.metric(
        "Unit Cost Filled",
        f"{quality['missing_unit_cost']:,}"
    )

    col7.metric(
        "Missing Region Handled",
        f"{quality['missing_region']:,}"
    )

    col8.metric(
        "Missing Segment Handled",
        f"{quality['missing_customer_segment']:,}"
    )

st.subheader("Download Reports")

st.caption(
    "Generate reports based on the current filter selection."
)

st.caption(
    f"Current filtered rows: {len(filtered_df):,}"
)

if "csv_report" not in st.session_state:
    st.session_state.csv_report = None

if "excel_report" not in st.session_state:
    st.session_state.excel_report = None

if "report_filter_state" not in st.session_state:
    st.session_state.report_filter_state = None

if st.session_state.report_filter_state != current_filter_state:
    st.session_state.csv_report = None
    st.session_state.excel_report = None

if st.button("Generate Reports"):
    with st.spinner("Generating reports..."):
        st.session_state.csv_report = generate_csv_report(filtered_df)
        st.session_state.excel_report = generate_excel_report(
            filtered_df,
            kpis
        )

        st.session_state.report_filter_state = current_filter_state


if (
    st.session_state.csv_report is not None
    and st.session_state.excel_report is not None
):
    col1, col2, _ = st.columns([1, 1, 3])

    with col1:
        st.download_button(
            label="Download CSV",
            data=st.session_state.csv_report,
            file_name="business_analysis.csv",
            mime="text/csv"
        )

    with col2:
        st.download_button(
            label="Download Excel Report",
            data=st.session_state.excel_report,
            file_name="business_analysis_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )