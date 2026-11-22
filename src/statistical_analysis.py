
import pandas as pd
from scipy.stats import (
    pearsonr,
    chi2_contingency,
    ttest_ind,
    f_oneway
)

# Load dataset
df = pd.read_csv("data/student-mat.csv", sep=";")

# Create Pass/Fail result
df["result"] = (df["G3"] >= 10).astype(int)

# Rename sex column for analysis
df = df.rename(columns={"sex": "Gender"})

results = []

results.append("STATISTICAL ANALYSIS")
results.append("=" * 50)

# 1. Pearson Correlation: Absences and Final Grade
r, p = pearsonr(df["absences"], df["G3"])

results.append("\n1. Pearson Correlation")
results.append(f"Correlation: {r:.4f}")
results.append(f"P-value: {p:.4f}")

# 2. Chi-square: Gender vs Pass/Fail
gender_table = pd.crosstab(df["Gender"], df["result"])
chi2, p, dof, expected = chi2_contingency(gender_table)

n = gender_table.to_numpy().sum()
cramers_v = (chi2 / n) ** 0.5

results.append("\n2. Chi-square Test: Gender vs Pass/Fail")
results.append(str(gender_table))
results.append(f"Chi-square: {chi2:.4f}")
results.append(f"Degrees of Freedom: {dof}")
results.append(f"P-value: {p:.4f}")
results.append(f"Cramer's V: {cramers_v:.4f}")

# 3. Welch's T-test: Gender vs Final Grade
male = df[df["Gender"] == "M"]["G3"]
female = df[df["Gender"] == "F"]["G3"]

t_stat, p = ttest_ind(
    male, female, equal_var=False
)

mean_difference = female.mean() - male.mean()

results.append("\n3. Welch's T-test: Gender vs Final Grade")
results.append(f"Male Mean: {male.mean():.2f}")
results.append(f"Female Mean: {female.mean():.2f}")
results.append(f"Mean Difference (Female - Male): {mean_difference:.2f}")
results.append(f"T-statistic: {t_stat:.4f}")
results.append(f"P-value: {p:.4f}")

# 4. Chi-square: Internet Access vs Pass/Fail
internet_table = pd.crosstab(df["internet"], df["result"])
chi2_internet, p_internet, dof_internet, expected = (
    chi2_contingency(internet_table)
)

results.append("\n4. Chi-square: Internet Access vs Pass/Fail")
results.append(str(internet_table))
results.append(f"Chi-square: {chi2_internet:.4f}")
results.append(f"P-value: {p_internet:.4f}")

# 5. ANOVA: Study Time Groups vs Final Grade
study_groups = [
    df[df["studytime"] == group]["G3"]
    for group in sorted(df["studytime"].unique())
]

f_stat, p_anova = f_oneway(*study_groups)

results.append("\n5. ANOVA: Study Time vs Final Grade")
results.append(f"F-statistic: {f_stat:.4f}")
results.append(f"P-value: {p_anova:.4f}")

# Save results
output = "\n".join(results)

with open("reports/statistical_results.txt", "w") as file:
    file.write(output)

print(output)
print("\nResults saved in reports/statistical_results.txt")
