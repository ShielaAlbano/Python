# Step 1: Standardize region names
data["region"] = (
    data["region"]
    .str.lower()  # Convert to lowercase
    .replace({
        "north zone": "north",
        "south area": "south",
        "eastern region": "east",
        "western region": "west"
    })
)

# Save the standardized data
data.to_csv("tire_data_standardized_regions.csv", index=False)

# Importance:
# - Ensures consistent region names, enabling accurate grouping and analysis by geography.
