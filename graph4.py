import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("merged_data.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(14,7))

# Axis 1 - NIFTY Close Price
plt.plot(df["Date"], df["Close"], color="blue", label="NIFTY Close Price")

# Create second axis
ax1 = plt.gca()
ax2 = ax1.twinx()

# Axis 2 - Sentiment
ax2.plot(df["Date"], df["Compound_Sentiment"], color="red", alpha=0.6, label="Sentiment Score")

# Labels
ax1.set_xlabel("Year")
ax1.set_ylabel("NIFTY Close Price", color="blue")
ax2.set_ylabel("Sentiment Score", color="red")

plt.title("Graph 4: Price vs Sentiment Trend (2017–Now)")

# Grid
plt.grid(True)

# Legend
line1, = ax1.get_lines()
line2, = ax2.get_lines()
plt.legend([line1, line2], ["Close Price", "Sentiment"], loc="upper left")

plt.show()
