import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)

def load_data():

    bike_quotes = pd.read_csv(
        os.path.join(
            BASE_DIR,
            "..",
            "data",
            "quotation_data",
            "acko_bike_quotation.csv"
        )
    )

    car_quotes = pd.read_csv(
        os.path.join(
            BASE_DIR,
            "..",
            "data",
            "quotation_data",
            "acko_car_quotation.csv"
        )
    )

    health_quotes = pd.read_csv(
        os.path.join(
            BASE_DIR,
            "..",
            "data",
            "quotation_data",
            "acko_health_quotation.csv"
        )
    )

    bike_claims = pd.read_csv(
        os.path.join(
            BASE_DIR,
            "..",
            "data",
            "claims_data",
            "acko_bike_claims.csv"
        )
    )

    car_claims = pd.read_csv(
        os.path.join(
            BASE_DIR,
            "..",
            "data",
            "claims_data",
            "acko_car_claims.csv"
        )
    )

    return (
        bike_quotes,
        car_quotes,
        health_quotes,
        bike_claims,
        car_claims
    )