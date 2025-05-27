# Store Sales Forecasting — Zindi Hackathon Project

## Overview

This project is part of the [Store Sales Forecasting Challenge for Beginners](https://zindi.africa/competitions/store-sales-forecasting-challenge-for-beginners) hosted on [Zindi Africa](https://zindi.africa/). The goal is to predict daily sales for different product categories across multiple stores using historical transaction data and related features.

I am building this project end-to-end, including:

- Data cleaning and merging
- Feature engineering (lags, rolling means, holidays, etc.)
- Model training using LightGBM
- Prediction generation and submission file creation

---

## Setup Instructions

Make sure you have Python 3.7+ installed. Install required libraries with:

```bash
pip install pandas numpy scikit-learn lightgbm joblib
```

---
## Dataset Files

| **File**               | **Description**                                                                                     | **Size**     |
|------------------------|-----------------------------------------------------------------------------------------------------|--------------|
| `test.csv`             | Resembles `train.csv` but **without** the target column. This is the dataset for model prediction.  | 2.6 MB       |
| `holidays.csv`         | Contains **holiday information** used to flag special dates.                                        | 1.8 KB       |
| `stores.csv`           | Contains details about **store locations, types, and clusters**.                                    | 864 B        |
| `dates.csv`            | Provides **calendar-based features** like day of week, day of year, etc.                            | 79.8 KB      |
| `SampleSubmission.csv` | Shows the **expected submission format** including the `ID` column layout.                          | 508.6 KB     |
| `train.csv`            | Main training dataset that **contains the target** sales values for model training.                 | 83.6 MB      |

---

## Project Structure

This project is organized into four main components:

| **Part**                    | **Details**                                                                                     |
|-----------------------------|--------------------------------------------------------------------------------------------------|
| 📁 `Preparation-of-Dataset` | Contains 5 scripts responsible for merging, cleaning, and engineering features from raw data.    |
| 📁 `Data-Inspection`        | Includes 2 scripts that verify whether the dataset has enough fields and records for modeling.   |
| 📄 `train.py`               | Handles model training using LightGBM and early stopping to avoid overfitting.                   |
| 📁 `prediction/`            | Uses the test dataset to generate predictions and save a final `Submission.csv` in required format. |

> A training-validation loss graph is also included to visualize the model’s learning performance.

---

