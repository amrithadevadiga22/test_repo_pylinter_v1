from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os


app = FastAPI()
#model = joblib.load("model.pkl")
# Make sure the model is loaded from the correct path

# Correct model path explicitly
model_path = "/app/app/model.pkl"  # Absolute path to model.pkl in the Docker container
print(f"Loading model from: {model_path}")
model = joblib.load(model_path)

class ShipmentFeatures(BaseModel):
    Warehouse_block: str
    Mode_of_Shipment: str
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: int
    Prior_purchases: int
    Product_importance: str
    Gender: str
    Discount_offered: int
    Weight_in_gms: int

@app.post("/predict")
def predict(features: ShipmentFeatures):
    data = pd.DataFrame([features.dict()])
    data = pd.get_dummies(data)
    # Align data with training features
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in data.columns:
            data[col] = 0
    data = data[model_features]
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
