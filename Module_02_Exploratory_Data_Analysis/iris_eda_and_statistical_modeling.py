"""
FlexiSAF Internship - Module 2 Project
Exploratory Data Analysis and Statistical Modeling of the Iris Dataset

Author: Samuel Adebanjo
Description:
    This script performs comprehensive Exploratory Data Analysis (EDA),
    inferential statistical testing, and predictive modeling on the Iris dataset.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, r2_score, mean_squared_error


def load_dataset() -> pd.DataFrame:
    """Load the Iris dataset from Seaborn public repository."""
    df = sns.load_dataset("iris")
    return df


def descriptive_statistics(df: pd.DataFrame) -> None:
    """Compute and display summary and group-level statistics."""
    print("=" * 60)
    print("1. DATASET OVERVIEW & SUMMARY STATISTICS")
    print("=" * 60)
    print("Dataset Shape:", df.shape)
    print("\nFirst 5 Records:")
    print(df.head())

    print("\nColumn Information & Missing Values:")
    print(df.info())
    print("\nMissing Values Count:\n", df.isnull().sum())

    numeric_cols = df.select_dtypes(include=[np.number])

    print("\nOverall Descriptive Statistics:")
    print(numeric_cols.describe().T)

    print("\nGroup Statistics by Species (Mean and Standard Deviation):")
    species_summary = df.groupby("species").agg(["mean", "std"])
    print(species_summary)


def correlation_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Generate the correlation matrix for numerical features."""
    print("\n" + "=" * 60)
    print("2. CORRELATION ANALYSIS")
    print("=" * 60)
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    print("Pearson Correlation Matrix:")
    print(corr)
    return corr


def hypothesis_testing(df: pd.DataFrame) -> None:
    """Conduct One-Way ANOVA tests across species for morphological traits."""
    print("\n" + "=" * 60)
    print("3. HYPOTHESIS TESTING (ONE-WAY ANOVA)")
    print("=" * 60)
    species_groups = [group["petal_length"].values for _, group in df.groupby("species")]
    f_val, p_val = stats.f_oneway(*species_groups)
    print(f"Petal Length Across Species -> F-statistic: {f_val:.4f}, p-value: {p_val:.4e}")
    if p_val < 0.05:
        print("Result: Statistically significant difference between species petal lengths (p < 0.05).")


def regression_modeling(df: pd.DataFrame) -> None:
    """Fit an Ordinary Least Squares linear regression model."""
    print("\n" + "=" * 60)
    print("4. STATISTICAL MODELING: LINEAR REGRESSION")
    print("=" * 60)
    x = df[["petal_length"]].values
    y = df["petal_width"].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    reg = LinearRegression()
    reg.fit(x_train, y_train)

    predictions = reg.predict(x_test)
    r2 = r2_score(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)

    print(f"Independent Variable : Petal Length")
    print(f"Dependent Variable   : Petal Width")
    print(f"Model Equation       : Petal Width = {reg.coef_[0]:.4f} * Petal Length + ({reg.intercept_:.4f})")
    print(f"R-squared (R2) Score : {r2:.4f}")
    print(f"Mean Squared Error   : {mse:.4f}")


def classification_modeling(df: pd.DataFrame) -> None:
    """Fit a multi-class Logistic Regression classifier to predict species."""
    print("\n" + "=" * 60)
    print("5. CLASSIFICATION MODELING: SPECIES PREDICTION")
    print("=" * 60)
    features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    x = df[features]
    y = df["species"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
    clf = LogisticRegression(max_iter=200, random_state=42)
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))


if __name__ == "__main__":
    iris_df = load_dataset()
    descriptive_statistics(iris_df)
    correlation_analysis(iris_df)
    hypothesis_testing(iris_df)
    regression_modeling(iris_df)
    classification_modeling(iris_df)
