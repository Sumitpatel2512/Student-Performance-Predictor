
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)

# Load dataset
data = pd.read_csv("data/student-mat.csv", sep=";")

# Create pass/fail target
# 1 = Pass, 0 = Fail
data["result"] = (data["G3"] >= 10).astype(int)

# Select input features
# G1 and G2 are earlier period grades.
# G3 is excluded to prevent target leakage.
features = [
    "age",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2"
]

X = data[features]
y = data["result"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Create Logistic Regression pipeline
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)
roc_auc = roc_auc_score(y_test, y_prob)

# Display results
print("\n===== LOGISTIC REGRESSION RESULTS =====")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print(f"ROC-AUC:   {roc_auc:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Create reports folder
Path("reports").mkdir(exist_ok=True)

# Plot confusion matrix
plt.figure(figsize=(7, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Fail", "Pass"],
    yticklabels=["Fail", "Pass"]
)

plt.title("Logistic Regression - Confusion Matrix")
plt.xlabel("Predicted Result")
plt.ylabel("Actual Result")
plt.tight_layout()
plt.savefig("reports/confusion_matrix.png", dpi=300)
plt.show()

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, label=f"ROC-AUC = {roc_auc:.3f}")
plt.plot([0, 1], [0, 1], linestyle="--")

plt.title("Logistic Regression - ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.tight_layout()
plt.savefig("reports/roc_curve.png", dpi=300)
plt.show()

# Save model
joblib.dump(model, "reports/student_performance_model.pkl")

# Save evaluation results
with open("reports/model_results.txt", "w") as file:
    file.write("LOGISTIC REGRESSION RESULTS\n")
    file.write(f"Training records: {len(X_train)}\n")
    file.write(f"Testing records: {len(X_test)}\n")
    file.write(f"Accuracy: {accuracy:.4f}\n")
    file.write(f"Precision: {precision:.4f}\n")
    file.write(f"Recall: {recall:.4f}\n")
    file.write(f"F1 Score: {f1:.4f}\n")
    file.write(f"ROC-AUC: {roc_auc:.4f}\n")
    file.write(f"Confusion Matrix:\n{cm}\n")
    file.write("\n" + classification_report(y_test, y_pred))

print("\nModel and results saved successfully!")
