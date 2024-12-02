
import pandas as pd

# Load the tire data
data = pd.read_csv("tire_data.csv")

# Step 1: Remove unwanted characters and standardize the format of tire sizes
data["tire_size"] = (
    data["tire_size"]
    .str.upper()  # Convert to uppercase
    .str.replace(r"[^A-Z0-9/]", "", regex=True)  # Remove non-alphanumeric characters
    .str.strip()  # Remove leading and trailing spaces
)

# Save the cleaned data
data.to_csv("tire_data_cleaned.csv", index=False)

# Importance:
# - Ensures consistent formatting of tire sizes, which is crucial for accurate analysis and matching.
