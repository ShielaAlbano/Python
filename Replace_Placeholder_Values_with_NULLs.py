# Step 1: Replace invalid placeholders with NaN
data.replace({"N/A": None, "Unknown": None, 0: None}, inplace=True)

# Save the updated data
data.to_csv("tire_data_placeholders_replaced.csv", index=False)

# Importance:
# - Marks missing or placeholder values correctly as NULL for better handling in downstream analyses.
