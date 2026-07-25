import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
df = pd.read_csv("merged_data.csv")

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Drop missing values for accurate calculation
df = df.dropna(subset=["Compound_Sentiment", "Price_Change_%"])

# Rolling 30-day correlation
df["Rolling_Correlation"] = df["Compound_Sentiment"].rolling(30).corr(df["Price_Change_%"])

# Plot
plt.figure(figsize=(14,7))
plt.plot(df["Date"], df["Rolling_Correlation"], color="purple")

plt.title("Graph 5C: 30-Day Rolling Correlation\nbetween Sentiment and Price Change")
plt.xlabel("Year")
plt.ylabel("Correlation (Sentiment ↔ Price Movement)")
plt.grid(True)
plt.axhline(0, color='black', linestyle='--', linewidth=1)

plt.show()
