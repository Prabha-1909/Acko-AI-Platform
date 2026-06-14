from ml_model.bike_premium_predict import predict_bike_claim

result = predict_bike_claim(
    30,
    5,
    3,
    150000,
    0,
    50,
    4,
    20000,
    8,
    1
)

print(result)