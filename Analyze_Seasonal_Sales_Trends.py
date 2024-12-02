import pandas as pd

# Load sales data
sales_data = pd.read_csv("sales_data.csv")

# Convert sale date to datetime
sales_data["sale_date"] = pd.to_datetime(sales_data["sale_date"])

# Extract the month for analysis
sales_data["sale_month"] = sales_data["sale_date"].dt.month

# Group by month and calculate total sales and revenue
seasonal_trends = sales_data.groupby("sale_month").agg(
    total_units_sold=("quantity_sold", "sum"),
    total_revenue=("revenue", "sum")
)

# Save the results to a CSV file
seasonal_trends.to_csv("seasonal_sales_trends.csv")

# Importance:
# - Reveals peak sales months, helping with inventory planning and marketing strategies.
