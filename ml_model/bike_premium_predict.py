import pickle
import numpy as np

with open("ml_model/bike_premium_model.pkl", "rb") as f:
    model = pickle.load(f)

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

    features = np.array([
        [
            customer_age,
            city_risk_score,
            vehicle_age_years,
            engine_cc,
            idv,
            ncb_percent,
            claim_history_count,
            num_addons
        ]
    ])

    premium = model.predict(features)[0]

    return {
        "predicted_premium": round(float(premium), 2)
    }