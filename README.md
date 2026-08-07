# Business Analytics & Reporting Platform

An interactive business analytics dashboard built with Python, Pandas, Streamlit, Plotly, and OpenPyXL.

The application transforms raw sales data into actionable business insights through data cleaning, KPI calculation, interactive filtering, performance analysis, and downloadable CSV/Excel reports.

## Features

- Automated data cleaning and validation
- Interactive date, region, category, and customer segment filters
- Revenue, profit, order, AOV, and profit margin KPIs
- Revenue and profit trend analysis
- Category and regional performance analysis
- Top product analysis
- Revenue vs profit relationship analysis
- Automated business insights
- Data quality summary
- CSV export
- Multi-sheet Excel report generation

## Business Metrics

The platform calculates:

- Total Revenue
- Total Profit
- Total Orders
- Average Order Value
- Profit Margin
- Product Performance
- Regional Performance
- Category Performance

## Data Processing

The application handles common data quality issues including:

- Duplicate records
- Invalid dates
- Missing unit prices
- Missing unit costs
- Missing regions
- Missing customer segments

Missing financial values are filled using product-level median values, while missing categorical values are preserved as `Unknown`.

## Tech Stack

- Python
- Pandas
- Streamlit
- Plotly
- OpenPyXL

## Project Structure

```text
business-analytics-platform/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sales_data.csv
│
└── utils/
    ├── analytics.py
    ├── charts.py
    ├── data_cleaning.py
    ├── data_loader.py
    ├── data_quality.py
    ├── filters.py
    ├── insights.py
    └── report_generator.py
```

## How It Works

The application follows a modular analytics pipeline:

1. Raw sales data is loaded from CSV.
2. Duplicate records and invalid dates are identified and handled.
3. Missing financial values are filled using product-level median values.
4. Missing categorical values are preserved as `Unknown`.
5. Revenue, cost, profit, and profit margin metrics are calculated.
6. User-selected filters are applied across the entire dashboard.
7. KPIs, charts, and business insights are recalculated dynamically.
8. Filtered results can be exported as CSV or as a formatted multi-sheet Excel report.

## Reporting

The Excel report contains five worksheets:

- Executive Summary
- KPIs
- Product Performance
- Regional Analysis
- Filtered Data

Financial fields are formatted automatically, column widths are adjusted for readability, and report contents reflect the active dashboard filters.

## Dashboard Analysis

The dashboard includes:

- Revenue and Profit Over Time
- Category Performance
- Regional Performance
- Top 10 Products by Revenue
- Revenue vs Profit by Product

Interactive Plotly charts allow users to inspect values and toggle individual metrics.

## Business Insights

The application automatically generates insights from the filtered dataset, including:

- Top-performing region by revenue
- Most profitable category
- Most profitable product
- Overall profit margin

These insights update dynamically whenever the dashboard filters change.

## Run Locally

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd business-analytics-platform
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

## Screenshots

Dashboard screenshots will be added after the final deployment.

## Live Demo

The live Streamlit application will be added here after deployment.