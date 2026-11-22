
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/student-mat.csv", sep=";")

print("\n========== DATASET OVERVIEW ==========")
print("First 5 Records:")
print(data.head())

print("\nDataset Shape:", data.shape)
print("\nDataset Information:")
data.info()

print("\nMissing Values:")
print(data.isnull().sum())

print("\nTotal Missing Values:", data.isnull().sum().sum())
print("Duplicate Records:", data.duplicated().sum())

print("\nStatistical Summary:")
print(data.describe())

# Create Pass/Fail column
# Passing grade is defined as 10 or above out of 20
data["result"] = (data["G3"] >= 10).astype(int)

print("\nPass/Fail Distribution:")
print(data["result"].value_counts())

# Correlation analysis
print("\nCorrelation with Final Grade:")
print(data[["studytime", "failures", "absences", "G1", "G2", "G3"]].corr()["G3"])

# Create reports folder output files
# Generate all graphs together
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Graph 1: Final Grade Distribution
sns.histplot(data["G3"], bins=10, ax=axes[0, 0])
axes[0, 0].set_title("Final Grade Distribution")
axes[0, 0].set_xlabel("Final Grade (G3)")
axes[0, 0].set_ylabel("Number of Students")

# Graph 2: Study Time vs Final Grade
study_avg = data.groupby("studytime")["G3"].mean()
study_avg.plot(kind="bar", ax=axes[0, 1])
axes[0, 1].set_title("Study Time vs Average Final Grade")
axes[0, 1].set_xlabel("Study Time")
axes[0, 1].set_ylabel("Average Grade")
axes[0, 1].tick_params(axis="x", rotation=0)

# Graph 3: Absences vs Final Grade
sns.scatterplot(data=data, x="absences", y="G3", ax=axes[1, 0])
axes[1, 0].set_title("Absences vs Final Grade")
axes[1, 0].set_xlabel("Absences")
axes[1, 0].set_ylabel("Final Grade")

# Graph 4: Correlation Heatmap
corr = data[["studytime", "failures", "absences", "G1", "G2", "G3"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=axes[1, 1])
axes[1, 1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("reports/eda_dashboard.png", dpi=300)
plt.show()

print("\nAll EDA graphs saved successfully!")
