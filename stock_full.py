import yfinance as yf
import pandas as pd

# Download NIFTY 50 data from 2017 to now
df = yf.download("^NSEI", start="2017-01-01", end=pd.Timestamp.today())

# Save dataset
df.to_csv("nifty_2017_to_now.csv")

print("NIFTY dataset created: nifty_2017_to_now.csv")
