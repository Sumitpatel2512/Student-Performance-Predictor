# Student Performance Predictor

A Probability & Statistics group project focused on analyzing student academic performance and predicting Pass/Fail outcomes using Python, Statistical Analysis, MySQL, and Machine Learning.

## Project Overview

This project analyzes student performance using the UCI Student Performance dataset. It explores factors related to academic results, performs statistical tests, and develops a Logistic Regression model to classify students as Pass or Fail.

**Note:** The dataset does not contain an actual dropout label. Therefore, this project predicts academic Pass/Fail outcomes rather than actual student dropout.

## Objectives

- Analyze student academic performance.
- Explore relationships between study time, failures, absences, and final grades.
- Perform statistical hypothesis testing.
- Store and analyze data using MySQL.
- Build a Logistic Regression classification model.
- Evaluate model performance using standard metrics.
- Compare model performance across gender groups.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- SciPy
- Scikit-learn
- MySQL
- SQL
- Visual Studio Code

## Dataset

**Source:** UCI Machine Learning Repository – Student Performance Dataset

- Subject used: Mathematics
- File: `student-mat.csv`
- Total records: 395
- Total attributes: 33

Dataset link: https://archive.ics.uci.edu/dataset/320/student

Reference:

Cortez, P. (2008). Student Performance [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T

License: CC BY 4.0.

## Project Structure

```text
Student_Performance_Predictor/
│
├── data/
│   ├── student-mat.csv
│   └── student-por.csv
│
├── src/
│   ├── data_analysis.py
│   ├── statistical_analysis.py
│   ├── model_training.py
│   ├── model_validation.py
│   ├── fairness_analysis.py
│   └── import_to_mysql.py
│
├── sql/
│   ├── analytical_queries.sql
│   └── er_diagram.mmd
│
├── reports/
│   ├── eda_dashboard.png
│   ├── er_diagram.png
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   ├── data_quality_log.txt
│   ├── statistical_results.txt
│   ├── model_results.txt
│   ├── fairness_results.txt
│   └── theory_vs_experiment.txt
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sumitpatel2512/Student-Performance-Predictor.git
cd Student-Performance-Predictor
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

Run the Python scripts from the project root directory.

### Exploratory Data Analysis

```bash
python src/data_analysis.py
```

### Statistical Analysis

```bash
python src/statistical_analysis.py
```

### Model Training

```bash
python src/model_training.py
```

### Model Validation

```bash
python src/model_validation.py
```

### Gender Fairness Analysis

```bash
python src/fairness_analysis.py
```

## Database

Database Name: `student_performance_db`

Tables:

- Students
- Courses
- Attendance
- Results

The database stores student information, course details, attendance records, and examination results.

The SQL analytical queries are available in:

`sql/analytical_queries.sql`

The Python MySQL import script is:

`src/import_to_mysql.py`

Configure your local MySQL server before running the import script.

## Statistical Methods

- Pearson Correlation
- Chi-Square Test
- Welch's Independent Samples T-Test
- One-Way ANOVA

## Machine Learning Model

**Algorithm:** Logistic Regression

**Target Variable:** Pass/Fail

Passing condition: G3 >= 10

Features used:

- Age
- Study Time
- Previous Failures
- Absences
- G1
- G2

The final grade G3 is excluded from the model input to prevent target leakage.

## Model Performance

| Metric | Result |
|---|---:|
| Accuracy | 88.61% |
| Precision | 94.00% |
| Recall | 88.68% |
| F1-Score | 91.26% |
| ROC-AUC | 96.81% |

## Project Reports and Visualizations

The `reports/` folder contains:

- Exploratory Data Analysis Dashboard
- Entity Relationship Diagram
- Confusion Matrix
- ROC Curve
- Statistical Analysis Results
- Model Results
- Fairness Analysis
- Theory vs Experiment Results
- Data Quality Log

## Limitations

- The dataset contains academic records from Portuguese secondary schools.
- The dataset does not provide an actual dropout label.
- The model predicts Pass/Fail outcomes, not actual dropout.
- The model results are based on the selected dataset and train-test split.
- Further validation is required before real-world use.

## Team Members

1. PATEL SHREY MANOJBHAI
2. PATEL SUMIT HEMANTBHAI
3. PATEL VEDANSHI SHAILESBHAI
4. PATEL VRAJ SUNILKUMAR
5. PATEL VIDHI PRASHANTBHAI

## Academic Project

**Course:** Probability & Statistics  
**Program:** B.Tech CSE  
**University:** JG University – School of Engineering

---

## Acknowledgement

We acknowledge the UCI Machine Learning Repository for providing the Student Performance dataset used in this academic project.