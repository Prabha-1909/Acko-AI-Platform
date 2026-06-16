import pickle
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(
    BASE_DIR,
    "bike_premium_model.pkl"
)

with open(model_path, "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]

feature_columns = model_data["feature_columns"]


def predict_bike_premium(
    customer_age,
    city_risk_score,
    vehicle_age_years,
    engine_cc,
    idv,
    ncb_percent,
    claim_history_count,
    num_addons
):

    input_data = {
        "customer_age": customer_age,
        "city_risk_score": city_risk_score,
        "city_tier": 1,
        "vehicle_age_years": vehicle_age_years,
        "engine_cc": engine_cc,
        "idv": idv,
        "ncb_percent": ncb_percent,
        "claim_history_count": claim_history_count,
        "num_addons": num_addons,

        "segment_Scooter": 0,
        "segment_Commuter": 1,
        "segment_Sports": 0,

        "fuel_type_Petrol": 1,
        "fuel_type_Electric": 0,

        "policy_type_Comprehensive": 1,
        "policy_type_Third Party": 0,

        "usage_type_Personal": 1,
        "usage_type_Commercial": 0
    }

    input_df = pd.DataFrame(
        [input_data]
    )

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    premium = model.predict(input_df)[0]

    return {
        "predicted_premium": round(float(premium), 2)
    }