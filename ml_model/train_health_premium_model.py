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
    "acko_health_quotation.csv"
)

df = pd.read_csv(csv_path)

df["gender"] = df["gender"].astype("category").cat.codes
df["city_tier"] = df["city_tier"].astype("category").cat.codes
df["bmi_category"] = df["bmi_category"].astype("category").cat.codes

X = df[
    [
        "age",
        "gender",
        "num_members",
        "city_tier",
        "bmi_category",
        "smoke",
        "has_pre_existing",
        "ncb_years",
        "sum_insured",
        "deductible",
        "num_addons",
        "has_maternity",
        "has_opd",
        "policy_tenure"
    ]
]

y = df["annual_premium"]

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

mse = mean_squared_error(y_test, predictions)

rmse = np.sqrt(mse)

mae = mean_absolute_error(y_test, predictions)

print("R2 Score :", round(r2, 4))
print("RMSE     :", round(rmse, 2))
print("MAE      :", round(mae, 2))

model_path = os.path.join(
    BASE_DIR,
    "health_premium_model.pkl"
)

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("Health Premium Model Saved")