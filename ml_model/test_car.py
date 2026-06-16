from ml_model.car_premium_predict import predict_car_premium

result = predict_car_premium(
    customer_age=35,
    city_risk_score=5,
    vehicle_age_years=4,
    engine_cc=1200,
    idv=500000,
    ncb_percent=20,
    claim_history_count=1,
    num_addons=2
)

print(result)