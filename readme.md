# 🫀 Heart Failure Risk Prediction App

This project is a **machine learning-based web application** built with **Flask** that predicts the **risk of heart failure** using clinical data from patients.  
It uses a **Logistic Regression model** trained on the [Heart Failure Clinical Records dataset](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data) from Kaggle.

---

## 🚀 Project Overview

Heart failure is a serious condition in which the heart is unable to pump blood effectively.  
This app allows users (e.g., doctors, researchers, or patients) to input clinical features and receive a **prediction of heart failure risk** — either **High Risk** or **Low Risk**.

The model was trained using:
- **Feature engineering** to create medically meaningful indicators.
- **SMOTE** to balance the dataset.
- **Grid Search with Cross-Validation** for hyperparameter tuning.
- **Logistic Regression** for interpretable predictions.

---

## 🧠 Model Pipeline Summary

1. **Data Source** – Kaggle Heart Failure Clinical Data  
2. **Feature Engineering** – Added interaction terms and clinical ratios  
3. **Preprocessing** – Standardization and class balancing using SMOTE  
4. **Model** – Logistic Regression with optimized hyperparameters  
5. **Deployment** – Flask web app for real-time predictions  

---

## ⚙️ Installation and Usage

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/heart-failure-predictor.git
   cd heart-failure-predictor
