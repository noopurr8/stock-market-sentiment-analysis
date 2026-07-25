import pandas as pd

# Load sentiment dataset
sentiment = pd.read_csv("sentiment_2017_to_now.csv")
sentiment["Date"] = pd.to_datetime(sentiment["Date"])

# Load NIFTY dataset (weird format)
raw = pd.read_csv("nifty_2017_to_now.csv")

# Drop the first two rows (Ticker, Date)
raw = raw.drop([0, 1]).reset_index(drop=True)

# Rename Price column to Date
raw.rename(columns={"Price": "Date"}, inplace=True)

# Convert Date to datetime
raw["Date"] = pd.to_datetime(raw["Date"])

# Convert other numeric columns
numeric_cols = ["Close", "High", "Low", "Open", "Volume"]
for col in numeric_cols:
    raw[col] = pd.to_numeric(raw[col], errors="coerce")

# Merge datasets
merged = pd.merge(raw, sentiment, on="Date", how="inner")

# Add price change %
merged["Price_Change_%"] = merged["Close"].pct_change() * 100

# Save
merged.to_csv("merged_data.csv", index=False)

print("Merged dataset created successfully: merged_data.csv")
