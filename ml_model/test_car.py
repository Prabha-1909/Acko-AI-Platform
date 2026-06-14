from ml_model.car_premium_predict import predict_car_claim

result = predict_car_claim(
    35,
    5,
    4,
    600000,
    1,
    35,
    5,
    50000,
    1
)

print(result)