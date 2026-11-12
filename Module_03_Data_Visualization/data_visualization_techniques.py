"""
FlexiSAF Internship - Module 3 Project
Data Visualization Techniques with Matplotlib and Seaborn

Author: Samuel Adebanjo
Description:
    Demonstrates core visualization techniques:
    1. Matplotlib line and scatter plots for time-series and correlation analysis.
    2. Seaborn histograms, box plots, and heatmaps for distribution and group comparisons.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_synthetic_data(samples: int = 100, seed: int = 42) -> pd.DataFrame:
    """Generate sample structured data for visualization demonstrations."""
    np.random.seed(seed)
    dates = pd.date_range(start="2024-01-01", periods=samples, freq="D")
    trend = np.linspace(10, 60, samples)
    noise = np.random.normal(0, 4, samples)
    values = trend + noise

    categories = np.random.choice(["Group A", "Group B", "Group C"], size=samples)
    feature_x = np.random.uniform(15, 95, samples)
    feature_y = 2.4 * feature_x + np.random.normal(0, 12, samples)

    return pd.DataFrame({
        "Date": dates,
        "Value": values,
        "Category": categories,
        "Feature_X": feature_x,
        "Feature_Y": feature_y
    })


def plot_matplotlib_visualizations(df: pd.DataFrame) -> None:
    """Render line and scatter charts using Matplotlib."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Line Plot: Metric evolution across time
    axes[0].plot(df["Date"], df["Value"], color="#1f77b4", linewidth=2, label="Trend Value")
    axes[0].set_title("Line Plot: Value Trend Over Time", fontsize=12, fontweight="bold")
    axes[0].set_xlabel("Date", fontsize=10)
    axes[0].set_ylabel("Metric Value", fontsize=10)
    axes[0].tick_params(axis="x", rotation=40)
    axes[0].grid(True, linestyle="--", alpha=0.5)
    axes[0].legend(loc="upper left")

    # Scatter Plot: Bivariate relationship
    scatter = axes[1].scatter(
        df["Feature_X"], df["Feature_Y"],
        c=df["Value"], cmap="viridis", alpha=0.85, edgecolors="k"
    )
    fig.colorbar(scatter, ax=axes[1], label="Value Intensity")
    axes[1].set_title("Scatter Plot: Feature X vs Feature Y", fontsize=12, fontweight="bold")
    axes[1].set_xlabel("Feature X", fontsize=10)
    axes[1].set_ylabel("Feature Y", fontsize=10)
    axes[1].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()


def plot_seaborn_visualizations(df: pd.DataFrame) -> None:
    """Render distribution and categorical comparisons using Seaborn."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Histogram with KDE
    sns.histplot(data=df, x="Value", kde=True, ax=axes[0], color="#6a3d9a", bins=15)
    axes[0].set_title("Histogram: Value Distribution with KDE", fontsize=12, fontweight="bold")
    axes[0].set_xlabel("Value", fontsize=10)
    axes[0].set_ylabel("Frequency", fontsize=10)

    # Box Plot for categorical comparison
    sns.boxplot(
        data=df, x="Category", y="Value",
        hue="Category", palette="Set2", legend=False, ax=axes[1]
    )
    axes[1].set_title("Box Plot: Metric Distribution by Category", fontsize=12, fontweight="bold")
    axes[1].set_xlabel("Category", fontsize=10)
    axes[1].set_ylabel("Value", fontsize=10)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    dataset = generate_synthetic_data()
    print("Dataset Preview:")
    print(dataset.head())
    plot_matplotlib_visualizations(dataset)
    plot_seaborn_visualizations(dataset)
