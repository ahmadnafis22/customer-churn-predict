
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field


# --------------------------------------------------
# 1. Project paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "churn_logistic_regression.joblib"
CONFIG_PATH = MODEL_DIR / "churn_config.joblib"


# --------------------------------------------------
# 2. Load model and configuration
# --------------------------------------------------
model = joblib.load(MODEL_PATH)
config = joblib.load(CONFIG_PATH)

THRESHOLD = config["threshold"]


# --------------------------------------------------
# 3. Create FastAPI application
# --------------------------------------------------
app = FastAPI(
    title="Telco Customer Churn Prediction API",
    description="Predict customer churn using Machine Learning.",
    version="1.0.0",
)


# --------------------------------------------------
# 4. Input schema
# --------------------------------------------------
class CustomerInput(BaseModel):
    # These columns must match the training dataset.
    gender: str
    SeniorCitizen: int = Field(ge=0, le=1)
    Partner: str
    Dependents: str
    tenure: int = Field(ge=0, le=100)
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float = Field(ge=0)
    TotalCharges: float = Field(ge=0)


# --------------------------------------------------
# 5. Home endpoint
# --------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to Telco Churn Prediction API!",
        "docs": "/docs",
    }


# --------------------------------------------------
# 6. Health endpoint
# --------------------------------------------------
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "threshold": THRESHOLD,
    }


# --------------------------------------------------
# 7. Prediction endpoint
# --------------------------------------------------
@app.post("/predict")
def predict_churn(data: CustomerInput):
    input_df = pd.DataFrame([data.model_dump()])

    # The saved pipeline handles preprocessing automatically.
    probability = float(model.predict_proba(input_df)[0, 1])

    prediction = int(probability >= THRESHOLD)

    return {
        "status": "success",
        "prediction": "Yes (Likely to Churn)" if prediction else "No (Likely to Stay)",
        "churn_probability": round(probability * 100, 2),
        "threshold": THRESHOLD,
    }
