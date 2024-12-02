import pandas as pd

# Load tire usage data
data = pd.read_csv("tire_usage.csv")

# Calculate tire lifespan in months
data["lifespan_months"] = ((pd.to_datetime(data["failure_date"]) - pd.to_datetime(data["production_date"])).dt.days / 30).round(1)

# Categorize lifespan into usage buckets
data["usage_category"] = pd.cut(
    data["mileage"],
    bins=[0, 20000, 40000, float("inf")],
    labels=["Low Usage", "Medium Usage", "High Usage"]
)

# Analyze average lifespan per usage category
lifespan_analysis = data.groupby("usage_category").agg(
    average_lifespan=("lifespan_months", "mean"),
    minimum_lifespan=("lifespan_months", "min"),
    maximum_lifespan=("lifespan_months", "max")
)

# Save the analysis results
lifespan_analysis.to_csv("tire_lifespan_analysis.csv")

# Importance:
# - Identifies how usage patterns affect tire lifespan.
# - Enables better product recommendations and proactive maintenance suggestions.
