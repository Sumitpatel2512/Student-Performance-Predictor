
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load dataset
df = pd.read_csv("data/student-mat.csv", sep=";")

# Create target variable
df["result"] = (df["G3"] >= 10).astype(int)

# Features and target
X = df[["age", "studytime", "failures", "absences", "G1", "G2"]]
y = df["result"]

# Keep Gender separately for fairness analysis
gender = df["sex"]

# Train-test split
X_train, X_test, y_train, y_test, gender_train, gender_test = (
    train_test_split(
        X, y, gender,
        test_size=0.20,
        random_state=42,
        stratify=y
    )
)

# Create and train model
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])

model.fit(X_train, y_train)

# Predict test results
y_pred = model.predict(X_test)

# Gender-based fairness analysis
results = []

results.append("GENDER-BASED FAIRNESS ANALYSIS")
results.append("=" * 55)

for group, label in [("F", "Female"), ("M", "Male")]:
    mask = gender_test == group

    actual = y_test[mask]
    predicted = pd.Series(y_pred, index=y_test.index)[mask]

    accuracy = accuracy_score(actual, predicted)
    precision = precision_score(
        actual, predicted, zero_division=0
    )
    recall = recall_score(
        actual, predicted, zero_division=0
    )

    predicted_pass_rate = predicted.mean() * 100
    actual_pass_rate = actual.mean() * 100

    results.append(f"\n{label} Students")
    results.append(f"Number of Students: {len(actual)}")
    results.append(f"Accuracy: {accuracy:.4f}")
    results.append(f"Pass Precision: {precision:.4f}")
    results.append(f"Pass Recall: {recall:.4f}")
    results.append(
        f"Predicted Pass Rate: {predicted_pass_rate:.2f}%"
    )
    results.append(
        f"Actual Pass Rate: {actual_pass_rate:.2f}%"
    )

# Save results
output = "\n".join(results)

with open("reports/fairness_results.txt", "w") as file:
    file.write(output)

print(output)
print("\nResults saved in reports/fairness_results.txt")
