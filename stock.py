import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download 1-year NIFTY 50 data
df = yf.download("^NSEI", period="1y")

# Calculate Moving Averages
df['MA10'] = df['Close'].rolling(window=10).mean()
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA100'] = df['Close'].rolling(window=100).mean()

# Plot the chart
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close Price', linewidth=2, color='purple')
plt.plot(df['MA10'], label='MA10', color='lightcoral')
plt.plot(df['MA20'], label='MA20', color='magenta')
plt.plot(df['MA50'], label='MA50', color='blue')
plt.plot(df['MA100'], label='MA100', color='cyan')

plt.title("NIFTY 50: Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.grid(True)
plt.show()
