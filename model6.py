import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("merged_data.csv")

# Drop missing values
df = df.dropna(subset=["Compound_Sentiment", "Price_Change_%"])

# Features (X) and target (y)
X = df[["Compound_Sentiment"]]
y = df["Price_Change_%"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Linear Regression Model Results")
print("---------------------------------")
print("Mean Squared Error:", mse)
print("R² Score:", r2)
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

# Plot: Actual vs Predicted
plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.xlabel("Actual Price Change (%)")
plt.ylabel("Predicted Price Change (%)")
plt.title("Model 6: Actual vs Predicted Price Change")
plt.grid(True)
plt.show()
