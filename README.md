# Telco Customer Churn Prediction

**An End-to-End Machine Learning Project with FastAPI and Streamlit**

An end-to-end machine learning project that predicts customer churn for a telecommunications company. The project covers data preprocessing, exploratory data analysis, model comparison, classification threshold tuning, model persistence, and deployment through a FastAPI backend with a Streamlit interface.

## Project Overview

Customer churn occurs when customers stop using a company's services. Identifying customers who are likely to leave helps businesses make better retention decisions.

This project uses the Telco Customer Churn dataset to build a binary classification model that estimates whether a customer is likely to churn.

The final model is a **Logistic Regression classifier** with a classification threshold of **0.30**, selected to improve the detection of customers likely to leave.

## Key Features

- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Analysis of class imbalance
- Training and comparison of multiple machine learning models
- Classification threshold tuning
- Model evaluation using multiple metrics
- Saved model artifacts using Joblib
- REST API built with FastAPI
- Interactive prediction interface built with Streamlit

## Tech Stack

- **Python** — Core programming language
- **Pandas & NumPy** — Data processing
- **Scikit-learn** — Preprocessing, model training, and evaluation
- **XGBoost** — Gradient boosting model comparison
- **Matplotlib & Seaborn** — Data visualization
- **Joblib** — Model persistence
- **FastAPI** — REST API development
- **Uvicorn** — ASGI server
- **Streamlit** — Interactive web interface
- **Requests** — HTTP communication between the frontend and API

## Dataset

The project uses the Telco Customer Churn dataset, which contains customer information such as:

- Customer demographics
- Contract type
- Internet and additional services
- Tenure
- Monthly charges
- Total charges
- Churn status

The target variable is `Churn`:

- `Yes` — The customer left the service.
- `No` — The customer stayed with the service.

The raw dataset is not included in the repository. Obtain the dataset separately and place it in the expected `data/` directory if you want to reproduce the notebook analysis.

## Machine Learning Workflow

### 1. Data Cleaning and Exploratory Data Analysis

- Inspected the dataset structure and data types.
- Handled missing or blank values in `TotalCharges`.
- Examined target distribution and class imbalance.
- Explored relationships between customer characteristics and churn.

### 2. Preprocessing

Prepared the features for machine learning, including categorical encoding and numerical feature scaling where required by the model pipeline.

### 3. Model Training and Comparison

Several classification algorithms were evaluated, including:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Models were compared using metrics suited to an imbalanced binary classification problem.

### 4. Model Selection and Threshold Tuning

Logistic Regression was selected as the final model. The classification threshold was set to `0.30` to increase sensitivity to potential churners.

A lower threshold can identify more potential churners, but it can also increase false-positive predictions. The appropriate threshold depends on the business cost of missing a customer who may leave versus contacting a customer who would have stayed.

### 5. Deployment

The trained model and configuration are saved using Joblib. The FastAPI backend exposes a prediction endpoint, while the Streamlit frontend provides an interactive interface for making predictions.

## Model Performance

The final model achieved the following results on the test set:

| Metric | Score |
|---|---:|
| Accuracy | 0.7500 |
| Precision | 0.5188 |
| Recall | 0.7893 |
| F1-score | 0.6261 |
| ROC-AUC | 0.8454 |

### Confusion Matrix

| | Predicted: No Churn | Predicted: Churn |
|---|---:|---:|
| **Actual: No Churn** | 571 | 205 |
| **Actual: Churn** | 59 | 221 |

### Interpretation

- **Recall (78.93%)**: The model identifies a substantial proportion of customers who actually churn.
- **Precision (51.88%)**: Some customers flagged as likely to churn will not actually leave.
- **ROC-AUC (0.8454)**: The model shows good ability to distinguish between churn and non-churn customers across classification thresholds.
- **Accuracy (75.00%)**: Overall proportion of correct predictions at the selected threshold.

For churn prediction, recall can be particularly important because failing to identify a customer who leaves may mean losing an opportunity to improve retention. However, precision and the cost of retention campaigns should also be considered.

## Project Structure

```text
customer-churn-prediction/
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── models/
│   ├── churn_logistic_regression.joblib
│   └── churn_config.joblib
├── notebooks/
│   └── churn_notebook.ipynb
├── data/
│   └── (dataset added locally)
├── .gitignore
├── requirements.txt
└── README.md
```

The exact model filenames and notebook filename should match the files in the repository. The `data/` directory is intended for local dataset files and may be excluded from Git.

## Getting Started

### Prerequisites

- Python 3.11 recommended
- Git
- A terminal such as PowerShell or Command Prompt

### 1. Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username after creating the repository.

```bash
git clone https://github.com/YOUR-USERNAME/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create a Virtual Environment

Using Python 3.11:

```bash
py -3.11 -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the FastAPI Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

Open the interactive API documentation at:

`http://127.0.0.1:8000/docs`

**Note:** The backend must be configured to load the model files from their actual locations. If your `main.py` uses different paths or module imports, adjust the command and paths accordingly.

### 5. Start the Streamlit Frontend

Open a second terminal, activate the same virtual environment, and run:

```bash
streamlit run frontend/app.py
```

If the frontend sends requests to the backend, make sure the backend is running and that the API URL configured in the frontend matches the local backend address.

## API Usage

The API provides a way for client applications to submit customer information and receive a churn prediction.

The exact endpoint, request fields, and response format depend on the implementation in `backend/main.py`.

To explore the available endpoints and request schemas, start the backend and visit:

`http://127.0.0.1:8000/docs`

## Limitations and Future Improvements

Potential improvements include:

- More systematic hyperparameter optimization
- Calibration of predicted probabilities
- Cost-sensitive threshold selection
- Model monitoring and data drift detection
- Unit and integration tests for the API
- Docker-based deployment
- Cloud deployment and CI/CD automation
- Explainability using SHAP or similar tools

## What I Learned

Through this project, I practiced:

- Building an end-to-end machine learning workflow
- Evaluating models on an imbalanced dataset
- Understanding precision-recall trade-offs
- Tuning a classification threshold based on business objectives
- Saving and loading trained models
- Building a REST API with FastAPI
- Connecting a Streamlit frontend to a machine learning API
- Organizing a machine learning project for GitHub

## Disclaimer

This project is intended for educational and portfolio purposes. Predictions are estimates and should not be treated as guarantees of future customer behavior.

## Author

**Your Name**

- GitHub: `https://github.com/YOUR-USERNAME`
- LinkedIn: `YOUR-LINKEDIN-URL`
