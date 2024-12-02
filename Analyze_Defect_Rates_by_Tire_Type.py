import pandas as pd

# Load the tire production dataset
data = pd.read_csv("tire_production.csv")

# Group by tire type and calculate defect rates
defect_analysis = (
    data.groupby("tire_type")
    .agg(
        total_produced=("defect_flag", "count"),  # Count total tires produced
        total_defects=("defect_flag", "sum")     # Sum defective tires
    )
    .assign(defect_rate=lambda x: (x["total_defects"] / x["total_produced"]) * 100)  # Calculate defect rate
    .sort_values(by="defect_rate", ascending=False)  # Sort by highest defect rate
)

# Save results to a CSV file
defect_analysis.to_csv("defect_rates_by_tire_type.csv")

# Importance:
# - This script identifies which tire types have the highest defect rates.
# - Helps in targeting specific tire types for quality improvement efforts.
