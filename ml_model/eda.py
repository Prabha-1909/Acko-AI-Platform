import pandas as pd

bike = pd.read_csv(
    "data/quotation_data/acko_bike_quotation.csv"
)

car = pd.read_csv(
    "data/quotation_data/acko_car_quotation.csv"
)

df = pd.read_csv(
    "data/quotation_data/acko_health_quotation.csv"
)

print(df.head())
print(df.columns.tolist())

print("\nBIKE COLUMNS:")
print(bike.columns.tolist())

print("\nCAR COLUMNS:")
print(car.columns.tolist())

print(df["annual_premium"].describe())

bike_df = pd.read_csv(
    "data/claims_data/acko_bike_claims.csv"
)

car_df = pd.read_csv(
    "data/claims_data/acko_car_claims.csv"
)

print("\nBIKE CLAIM COLUMNS:")
print(bike_df.columns.tolist())

print("\nCAR CLAIM COLUMNS:")
print(car_df.columns.tolist())

