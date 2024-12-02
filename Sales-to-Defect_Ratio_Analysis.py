import pandas as pd

# Load sales and defect data
sales_data = pd.read_csv("sales_data.csv")
defect_data = pd.read_csv("defect_data.csv")

# Group and merge sales and defect summaries
sales_summary = sales_data.groupby("tire_type").agg(total_sales=("quantity_sold", "sum"))
defect_summary = defect_data.groupby("tire_type").agg(total_defects=("defect_flag", "sum"))

# Merge datasets
sales_defect_ratio = pd.merge(sales_summary, defect_summary, on="tire_type", how="inner")
sales_defect_ratio["sales_to_defect_ratio"] = sales_defect_ratio["total_sales"] / sales_defect_ratio["total_defects"]

# Save the results
sales_defect_ratio.to_csv("sales_to_defect_ratio.csv")

# Importance:
# - Evaluates the relationship between sales and defect rates to identify problematic tire types.
