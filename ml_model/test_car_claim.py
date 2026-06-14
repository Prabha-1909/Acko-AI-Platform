from ml_model.car_claim_predict import predict_car_claim

result = predict_car_claim(
    damage_severity_score=7,
    num_parts_affected=4,
    vehicle_age_years=5,
    idv=600000,
    city_risk_score=8,
    previous_claims_count=1,
    policy_age_months=20
)

print(result)