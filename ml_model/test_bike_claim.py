from ml_model.bike_claim_predict import predict_bike_claim

result = predict_bike_claim(
    damage_severity_score=6,
    num_parts_affected=3,
    vehicle_age_years=4,
    idv=90000,
    city_risk_score=7,
    previous_claims_count=1,
    policy_age_months=18
)

print(result)