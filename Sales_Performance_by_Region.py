import pandas as pd

# Load sales data
data = pd.read_csv("sales_data.csv")

# Group by region and tire type
regional_performance = data.groupby(["region", "tire_type"]).agg(
    total_units_sold=("quantity_sold", "sum"),
    total_revenue=("revenue", "sum"),
    average_price=("sale_price", "mean")
)

# Save the results
regional_performance.to_csv("regional_sales_performance.csv")

# Importance:
# - Identifies high-performing regions and products, supporting targeted marketing and resource allocation.
