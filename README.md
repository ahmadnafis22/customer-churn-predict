# 📊 Telco Customer Churn Prediction & FastAPI Deployment

<p align="center">
  <b>An end-to-end Machine Learning project to predict customer churn, handle class imbalance, and deploy a production-ready API using FastAPI.</b>
</p>

---

## 🇺🇸 English Section

### 🚀 Overview
Customer churn is a critical challenge for telecom companies. This project builds an end-to-end Machine Learning pipeline to predict whether a customer is likely to leave the service. It covers data preprocessing, handling class imbalance using **SMOTE**, training and evaluating multiple models, and deploying the best-performing model via a **FastAPI** backend.

### 🛠️ Tech Stack & Libraries
* **Python** (Core logic)
* **Scikit-Learn** (Preprocessing, Machine Learning models)
* **XGBoost** (Ensemble modeling)
* **Imbalanced-learn (SMOTE)** (Handling class imbalance)
* **FastAPI & Uvicorn** (API development & deployment)
* **Joblib** (Model persistence)
* **Pandas & NumPy** (Data manipulation)

### 📈 Workflow & Methodology
1. **Data Preprocessing & Cleaning:** Handled missing values, encoded categorical features, and scaled numerical variables.
2. **Handling Class Imbalance:** Applied **SMOTE** exclusively on the training dataset to prevent data leakage and improve minority class detection.
3. **Model Training & Evaluation:** Trained and compared 4 models:
   * Logistic Regression
   * Decision Tree
   * Random Forest
   * XGBoost
4. **Model Selection:** **Logistic Regression** was chosen as the production model due to its superior **Recall (0.74)**, ensuring the business minimizes false negatives (undetected churners).
5. **Deployment:** Saved the model using `joblib` and built a robust `FastAPI` endpoint with dynamic feature alignment (`reindex` using `feature_names_in_`) to prevent schema mismatch errors.

### 🚀 How to Run the Project Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/customer-churn-prediction.git](https://github.com/your-username/customer-churn-prediction.git)
   cd customer-churn-prediction