import pandas as pd
import numpy as np

# Load sales data
data = pd.read_csv("sales_data.csv")

# Calculate the correlation between price and quantity sold
correlation = data.groupby("tire_type").apply(
    lambda df: np.corrcoef(df["sale_price"], df["quantity_sold"])[0, 1]
)

# Convert the correlation results to a DataFrame
correlation_df = correlation.reset_index(name="price_sales_correlation")

# Save the correlation analysis
correlation_df.to_csv("price_sales_correlation.csv")

# Importance:
# - Identifies how price changes affect sales volume for each tire type.
# - Provides insights for pricing strategy optimization.
