# Calculate revenue by tire type
tire_revenue = data.groupby("tire_type")["revenue"].sum()

# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(tire_revenue.index, tire_revenue.values, color="orange")
plt.title("Revenue by Tire Type")
plt.xlabel("Tire Type")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Importance:
# - Highlights the top revenue-generating tire types for strategic focus.
