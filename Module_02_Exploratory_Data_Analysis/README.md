# Module 2: Exploratory Data Analysis & Statistical Modeling

**Program:** FlexiSAF Data Science Internship  
**Author:** Samuel Adebanjo  
**Focus Area:** Data Profiling, Descriptive Statistics, Hypothesis Testing & Predictive Modeling  

---

## 1. Project Overview
This project provides a comprehensive exploratory data analysis (EDA) and statistical modeling workflow on the **Iris dataset**. The objective is to evaluate morphological differences among three iris species (*Setosa*, *Versicolor*, and *Virginica*) and quantify the predictive power of anatomical traits.

---

## 2. Methodology & Key Stages

### Stage 1: Data Inspection & Summary Statistics
- Checked schema, missing values, and data integrity.
- Evaluated central tendency (mean, median, mode) and dispersion (standard deviation, variance, interquartile range).
- Conducted species-level aggregations to highlight anatomical divergence.

### Stage 2: Correlation & Feature Association
- Calculated Pearson correlation coefficients across all four numerical dimensions.
- Observed strong positive association between `petal_length` and `petal_width` ($r \approx 0.96$).
- Identified negative correlation between `sepal_width` and petal dimensions.

### Stage 3: Inferential Statistics (One-Way ANOVA)
- Executed One-Way ANOVA tests across species for all morphological traits.
- Confirmed statistically significant differences between species ($p < 0.001$), demonstrating that petal dimensions provide distinct boundaries between classes.

### Stage 4: Statistical Modeling
1. **Linear Regression (Petal Morphology):**
   - Modeled `petal_width` as a function of `petal_length`.
   - Achieved high goodness-of-fit ($R^2 > 0.90$), indicating a strong linear relationship.
2. **Species Classification (Logistic Regression):**
   - Evaluated a multi-class logistic regression model using an 80/20 train-test split.
   - Evaluated accuracy, precision, recall, and F1-score across all three species.

---

## 3. Project Structure
- `iris_eda_and_statistical_modeling.ipynb`: Interactive Jupyter Notebook containing exploratory steps and outputs.
- `iris_eda_and_statistical_modeling.py`: Modular Python script for automated execution.

---

## 4. How to Run
```bash
# Execute standalone script
python Module_02_Exploratory_Data_Analysis/iris_eda_and_statistical_modeling.py

# Or launch Jupyter Notebook
jupyter notebook Module_02_Exploratory_Data_Analysis/iris_eda_and_statistical_modeling.ipynb
```
