from ml_model.bike_premium_predict import predict_bike_premium

result = predict_bike_premium(
    customer_age=30,
    city_risk_score=5,
    vehicle_age_years=3,
    engine_cc=125,
    idv=100000,
    ncb_percent=20,
    claim_history_count=1,
    num_addons=1
)

print(result)