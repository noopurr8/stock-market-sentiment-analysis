import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("merged_data.csv")

# Drop missing values
df = df.dropna(subset=["Compound_Sentiment", "Price_Change_%"])

# Create UP/DOWN target
df["Direction"] = df["Price_Change_%"].apply(lambda x: 1 if x > 0 else 0)

# Features and target
X = df[["Compound_Sentiment"]]
y = df["Direction"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)

print("Classification Model (UP/DOWN) Results")
print("---------------------------------------")
print("Accuracy:", acc)
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(cr)

# Plot confusion matrix
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Up/Down Prediction")
plt.show()
