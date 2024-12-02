# Step 1: Fill missing sale prices with the average price per tire type
data["sale_price"] = data.groupby("tire_type")["sale_price"].transform(
    lambda x: x.fillna(x.mean())
)

# Save the imputed data
data.to_csv("tire_data_imputed_prices.csv", index=False)

# Importance:
# - Ensures missing sale prices are filled sensibly, avoiding gaps in revenue calculations.
