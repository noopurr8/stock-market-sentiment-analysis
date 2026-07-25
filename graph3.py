import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("merged_data.csv")

# Select only numeric columns for correlation
numeric_df = df[["Close", "High", "Low", "Open", "Volume",
                 "Positive", "Negative", "Neutral",
                 "Compound_Sentiment", "Price_Change_%"]]

# Compute correlation matrix
corr = numeric_df.corr()

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Graph 3: Correlation Heatmap of Market & Sentiment Features")
plt.show()
