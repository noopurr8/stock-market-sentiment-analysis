import pandas as pd
import matplotlib.pyplot as plt

# Load merged dataset
df = pd.read_csv("merged_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Plot Close price
plt.figure(figsize=(14,6))
plt.plot(df["Date"], df["Close"], label="NIFTY Close Price")

# Plot Sentiment
plt.plot(df["Date"], df["Compound_Sentiment"], label="Sentiment Score", alpha=0.7)

plt.xlabel("Date")
plt.ylabel("Value")
plt.title("NIFTY Close Price vs Sentiment (2017–Now)")
plt.legend()
plt.grid(True)
plt.show()
