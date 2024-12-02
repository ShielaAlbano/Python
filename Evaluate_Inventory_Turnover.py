import pandas as pd

# Load inventory data
inventory_data = pd.read_csv("inventory_data.csv")

# Calculate turnover rate
inventory_data["turnover_rate"] = inventory_data["units_sold"] / (
    inventory_data["starting_inventory"] + inventory_data["replenishments"] - inventory_data["ending_inventory"]
)

# Group by tire type and calculate average turnover rate
turnover_analysis = inventory_data.groupby("tire_type").agg(
    average_turnover=("turnover_rate", "mean")
)

# Save the analysis to a CSV file
turnover_analysis.to_csv("inventory_turnover_analysis.csv")

# Importance:
# - Measures inventory efficiency to optimize stock levels and reduce costs.
