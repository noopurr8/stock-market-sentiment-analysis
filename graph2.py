import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv("merged_data.csv")

# Drop rows with missing values
df = df.dropna(subset=["Compound_Sentiment", "Price_Change_%"])

# Extract values
x = df["Compound_Sentiment"]
y = df["Price_Change_%"]

# Scatter plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, alpha=0.5, label="Data points")

# Trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--", label="Trendline")

plt.xlabel("Sentiment Score (Compound)")
plt.ylabel("Price Change (%)")
plt.title("Graph 2: Sentiment vs Price Change Correlation")
plt.legend()
plt.grid(True)
plt.show()
