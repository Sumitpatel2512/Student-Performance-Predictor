
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load dataset
data = pd.read_csv("data/student-mat.csv", sep=";")

# Target variable
data["result"] = (data["G3"] >= 10).astype(int)

# Features
features = ["age", "studytime", "failures", "absences", "G1", "G2"]

X = data[features]
y = data["result"]

# Same train-test split as model training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Model
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train
model.fit(X_train, y_train)

# Predictions
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# Compare performance
train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, test_pred)

print("\n===== THEORY VS EXPERIMENT =====")
print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy:  {test_accuracy:.4f}")

print(f"\nTraining Precision: {precision_score(y_train, train_pred):.4f}")
print(f"Testing Precision:  {precision_score(y_test, test_pred):.4f}")

print(f"\nTraining Recall: {recall_score(y_train, train_pred):.4f}")
print(f"Testing Recall:  {recall_score(y_test, test_pred):.4f}")

print(f"\nTraining F1 Score: {f1_score(y_train, train_pred):.4f}")
print(f"Testing F1 Score:  {f1_score(y_test, test_pred):.4f}")

gap = train_accuracy - test_accuracy
print(f"\nAccuracy Gap: {gap:.4f}")

if gap > 0.10:
    print("Possible overfitting detected.")
else:
    print("No large training-testing accuracy gap detected.")

# Save results
with open("reports/theory_vs_experiment.txt", "w") as file:
    file.write(f"Training Accuracy: {train_accuracy:.4f}\n")
    file.write(f"Testing Accuracy: {test_accuracy:.4f}\n")
    file.write(f"Accuracy Gap: {gap:.4f}\n")

print("\nResults saved successfully!")
