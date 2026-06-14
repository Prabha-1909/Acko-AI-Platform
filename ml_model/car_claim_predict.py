import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)

amount_model_path = os.path.join(
    BASE_DIR,
    "car_claim_amount_model.pkl"
)

approval_model_path = os.path.join(
    BASE_DIR,
    "car_claim_approval_model.pkl"
)

with open(amount_model_path, "rb") as f:
    amount_model = pickle.load(f)

with open(approval_model_path, "rb") as f:
    approval_model = pickle.load(f)


def predict_car_claim(
    damage_severity_score,
    num_parts_affected,
    vehicle_age_years,
    idv,
    city_risk_score,
    previous_claims_count,
    policy_age_months
):

    features = np.array([
        [
            damage_severity_score,
            num_parts_affected,
            vehicle_age_years,
            idv,
            city_risk_score,
            previous_claims_count,
            policy_age_months
        ]
    ])

    claim_amount = amount_model.predict(features)[0]

    approval_probability = approval_model.predict_proba(features)[0][1]

    return {
        "predicted_claim_amount": round(float(claim_amount), 2),
        "approval_probability": round(float(approval_probability * 100), 2)
    }