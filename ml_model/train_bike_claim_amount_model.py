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
    "claims_data",
    "acko_bike_claims.csv"
)

df = pd.read_csv(csv_path)

X = df[
    [
        "damage_severity_score",
        "num_parts_affected",
        "vehicle_age_years",
        "idv",
        "city_risk_score",
        "previous_claims_count",
        "policy_age_months"
    ]
]

y = df["claim_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)

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

model_path = os.path.join(
    BASE_DIR,
    "bike_claim_amount_model.pkl"
)

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("Bike Claim Amount Model Saved")