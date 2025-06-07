# 💻 Laptop Price Predictor — A Machine Learning Web App

A data-driven machine learning project that predicts the **price of a laptop** based on its specifications. This web application uses a trained regression model and is built with **Flask** and **Scikit-learn**, and deployed via **Railway**.

**Live Demo**: [Laptop Price Predictor Web App](https://web-production-5d5f.up.railway.app/)

---

## Objective

To build an end-to-end machine learning web app that:
- Predicts laptop prices based on user-input features.
- Helps buyers, sellers, or tech enthusiasts understand fair pricing.
- Demonstrates a complete ML pipeline — from data preprocessing to deployment.

---

## Tools & Technologies

| Area              | Tools & Libraries                             |
|-------------------|-----------------------------------------------|
| Programming       | Python                                        |
| Data Handling     | Pandas, NumPy                                 |
| Visualization     | Matplotlib, Seaborn                           |
| Machine Learning  | Scikit-learn                                  |
| Web Development   | Flask                                         |
| Deployment        | Railway                                       |
| Dev Environment   | Jupyter Notebook, PyCharm                    |

---

## Project Workflow

### 1. Data Cleaning
- Loaded raw laptop dataset.
- Handled missing values and formatting issues.
- Converted binary attributes (`Touchscreen`, `IPS`) to numerical (0/1).

### 2. Feature Engineering
- Extracted screen size from resolution.
- Computed **PPI (Pixels Per Inch)** as a derived feature.
- Converted `HDD`, `SSD` storage columns to integers.

### 3. Exploratory Data Analysis (EDA)
- Visualized distributions, correlations, and outliers.
- Identified influential features on price.

### 4. Model Building
- Tested multiple regression models including:
  - **Linear Regression**
  - **Random Forest Regressor**
- Evaluated using:
  - R² Score
  - Cross-validation

### 5. Flask Integration
- Created an interactive web form using Jinja2 templating.
- Integrated the trained model to make real-time predictions from user inputs.

---

## 🔍 Features Used for Prediction

- **Brand** 
- **Laptop Type** (Ultrabook, Gaming, etc.)
- **RAM** (GB)
- **Weight** (kg)
- **Touchscreen** (Yes/No)
- **IPS Panel** (Yes/No)
- **Screen Size** (inches)
- **Screen Resolution** (e.g., 1920x1080)
- **CPU Brand**
- **Storage** (HDD & SSD in GB)
- **GPU Brand**
- **Operating System**

---

## Results & Insights

- **Random Forest Regressor** performed best with highest R² score.
- **Brand, RAM, CPU**, and **PPI** were major contributors to price prediction.
- Proper feature engineering (especially PPI) significantly improved accuracy.

---

## Deployment

This application is deployed on **[Railway](https://railway.app/)**, a simple and fast cloud hosting platform.
