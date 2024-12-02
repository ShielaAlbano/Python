import pandas as pd

# Load defect data
data = pd.read_csv("defect_data.csv")

# Group by material type and calculate defect rates
material_defect_rate = data.groupby("material_type").agg(
    total_produced=("defect_flag", "count"),
    defect_count=("defect_flag", "sum")
).assign(
    defect_rate=lambda x: (x["defect_count"] / x["total_produced"]) * 100
)

# Save the results
material_defect_rate.to_csv("material_defect_rate.csv")

# Importance:
# - Highlights materials that may require improvement for quality control.
