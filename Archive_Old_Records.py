# Step 1: Identify records older than 5 years
archived_data = data[data["production_date"] < pd.Timestamp.now() - pd.DateOffset(years=5)]

# Save archived records to a separate file
archived_data.to_csv("tire_data_archive.csv", index=False)

# Remove old records from the main dataset
data = data[data["production_date"] >= pd.Timestamp.now() - pd.DateOffset(years=5)]
data.to_csv("tire_data_active.csv", index=False)

# Importance:
# - Optimizes the active database for current operations while preserving historical data for reference.
