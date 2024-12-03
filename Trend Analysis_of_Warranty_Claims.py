
# Aggregate warranty claims by year
data["claim_date"] = pd.to_datetime(data["claim_date"])
data["claim_year"] = data["claim_date"].dt.year
warranty_trends = data.groupby("claim_year")["claim_id"].count()

# Plot the trend
plt.figure(figsize=(12, 6))
plt.plot(warranty_trends.index, warranty_trends.values, marker="o", linestyle="-", color="green")
plt.title("Yearly Warranty Claims Trends")
plt.xlabel("Year")
plt.ylabel("Total Claims")
plt.grid(True)
plt.tight_layout()
plt.show()

# Importance:
# - Tracks claims over time to assess product reliability.
