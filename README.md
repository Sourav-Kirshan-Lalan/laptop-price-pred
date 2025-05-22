# laptop-price-pred
# Laptop Price Predictor

## Overview
This Jupyter notebook analyzes laptop specifications and builds a foundation for price prediction through exploratory data analysis (EDA) and data preprocessing. The project uses Python data science libraries to process and visualize laptop features like RAM, weight, screen size, and company brand.

## Dataset
**File:** `laptop_data.csv`  
**Features:**
- Company (Manufacturer)
- TypeName (Laptop category)
- Inches (Screen size)
- ScreenResolution
- CPU 
- RAM 
- Memory (Storage)
- GPU
- OpSys (Operating System)
- Weight
- Price (Target variable)

## Key Steps

### 1. Data Loading & Initial Inspection
- Imports essential libraries (Pandas, NumPy, Matplotlib/Seaborn)
- Loads dataset and displays first 5 rows
- Checks dataset dimensions (1303 rows × 12 columns)
- Examines data types and missing values

### 2. Data Cleaning
- Removes unnecessary "Unnamed: 0" column
- Converts:
  - RAM from string ("8GB") to integer
  - Weight from string ("1.37kg") to float
- Checks for duplicates and missing values (none found)

### 3. Exploratory Data Analysis
**Key Visualizations:**
- Price distribution using distplot
- Company distribution with bar plot
- Laptop type distribution
- Manufacturer vs. Price relationships

## Usage
1. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn
