import pandas as pd

# Load warranty claims data
claims = pd.read_csv("warranty_claims.csv")

# Calculate total claims and average claim amount per tire type
warranty_analysis = claims.groupby("tire_type").agg(
    total_claims=("claim_id", "count"),
    total_claim_amount=("claim_amount", "sum"),
    average_claim_amount=("claim_amount", "mean")
)

# Save the results
warranty_analysis.to_csv("warranty_claim_analysis.csv")

# Importance:
# - Identifies tire types with the highest warranty costs, helping refine product design and warranty policies.
