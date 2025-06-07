# 💻 Laptop Price Predictor — A Machine Learning Project

## Project Explanation

The **Laptop Price Predictor** is a data-driven machine learning project designed to estimate the price of laptops based on various hardware and brand specifications. The primary goal is to provide users — whether buyers, sellers, or analysts — with a tool that can predict the fair market price of a laptop configuration using supervised learning techniques.

## Live Demo: https://web-production-5d5f.up.railway.app/
## Objective

To build a regression model that accurately predicts laptop prices from a dataset of laptop specifications by following a complete machine learning pipeline — from preprocessing to model evaluation.

---

## Tools and Technologies

- **Python** – Programming language
- **Pandas & NumPy** – Data manipulation
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Machine learning
- **Jupyter Notebook** – Development environment

---

## Project Workflow

### 1. **Data Cleaning**
- Loaded raw laptop data.
- Handled missing values and inconsistent formats.
- Converted binary attributes (like touchscreen, IPS) into 0/1.

### 2. **Feature Engineering**
- Extracted screen size from resolution.
- Converted storage columns (HDD/SSD) to numeric.
- Created new features like PPI (pixels per inch) for better model accuracy.

### 3. **Exploratory Data Analysis (EDA)**
- Visualized relationships between features and price.
- Checked feature distributions, correlations, and outliers.

### 4. **Model Building**
- Tested multiple regression models including:
  - **Linear Regression**
  - **Random Forest Regressor**
- Performed train/test split and evaluated with:
  - R² Score
  - Cross-validation

### 5. **Prediction**
- Final model can predict prices based on new input features.

---

## Sample Features Used

- Brand (Company)
- Laptop Type (Ultrabook, Gaming, etc.)
- RAM (in GB)
- Weight
- Touchscreen
- IPS Panel
- Screen Size
- Resolution
- CPU Brand
- Storage (HDD & SSD)
- GPU
- Operating System

---

## Results & Insights

- Random Forest Regressor outperformed other models with the best R² score.
- Features like brand, RAM, CPU, and display resolution had a significant impact on price.
- Proper feature engineering (like PPI) greatly enhanced model accuracy.


