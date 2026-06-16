import pandas as pd
import pickle
import os
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error
)

BASE_DIR = os.path.dirname(__file__)

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "quotation_data",
    "acko_car_quotation.csv"
)

df = pd.read_csv(csv_path)

df = pd.get_dummies(
    df,
    columns=[
        "segment",
        "fuel_type",
        "policy_type"
    ]
)

feature_columns = [
    "customer_age",
    "city_risk_score",
    "city_tier",
    "vehicle_age_years",
    "engine_cc",
    "idv",
    "ncb_percent",
    "claim_history_count",
    "num_addons"
]

encoded_columns = [
    col for col in df.columns
    if col.startswith("segment_")
    or col.startswith("fuel_type_")
    or col.startswith("policy_type_")
]

feature_columns = feature_columns + encoded_columns

X = df[feature_columns]

y = df["annual_premium"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=500,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(X_test)

r2 = r2_score(
    y_test,
    predictions
)

mse = mean_squared_error(
    y_test,
    predictions
)

rmse = np.sqrt(mse)

mae = mean_absolute_error(
    y_test,
    predictions
)

print("R2 Score :", round(r2, 4))
print("RMSE     :", round(rmse, 2))
print("MAE      :", round(mae, 2))

model_data = {
    "model": model,
    "feature_columns": feature_columns
}

model_path = os.path.join(
    BASE_DIR,
    "car_premium_model.pkl"
)

with open(model_path, "wb") as f:
    pickle.dump(model_data, f)

print("Car Premium Model Saved")