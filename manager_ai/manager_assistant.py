import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)

ROOT_DIR = os.path.abspath(
    os.path.join(
        BASE_DIR,
        ".."
    )
)


def load_manager_data():

    bike_claims = pd.read_csv(
        os.path.join(
            ROOT_DIR,
            "data",
            "claims_data",
            "acko_bike_claims.csv"
        )
    )

    car_claims = pd.read_csv(
        os.path.join(
            ROOT_DIR,
            "data",
            "claims_data",
            "acko_car_claims.csv"
        )
    )

    bike_quotes = pd.read_csv(
        os.path.join(
            ROOT_DIR,
            "data",
            "quotation_data",
            "acko_bike_quotation.csv"
        )
    )

    car_quotes = pd.read_csv(
        os.path.join(
            ROOT_DIR,
            "data",
            "quotation_data",
            "acko_car_quotation.csv"
        )
    )

    health_quotes = pd.read_csv(
        os.path.join(
            ROOT_DIR,
            "data",
            "quotation_data",
            "acko_health_quotation.csv"
        )
    )

    return (
        bike_claims,
        car_claims,
        bike_quotes,
        car_quotes,
        health_quotes
    )


def ask_manager(question):

    question = question.lower()

    (
        bike_claims,
        car_claims,
        bike_quotes,
        car_quotes,
        health_quotes
    ) = load_manager_data()

    all_claims = pd.concat(
        [
            bike_claims.assign(vehicle_type="bike"),
            car_claims.assign(vehicle_type="car")
        ],
        ignore_index=True
    )

    all_quotes = pd.concat(
        [
            bike_quotes.assign(vehicle_type="bike"),
            car_quotes.assign(vehicle_type="car"),
            health_quotes.assign(vehicle_type="health")
        ],
        ignore_index=True
    )

    if "how many" in question and "car claims" in question:

        total = len(car_claims)

        return f"There are {total:,} car claims in the dataset."

    if "how many" in question and "bike claims" in question:

        total = len(bike_claims)

        return f"There are {total:,} bike claims in the dataset."

    if "average payout" in question and "bike" in question:

        avg = bike_claims["claim_amount"].mean()

        return f"The average payout for bike claims is ₹{avg:,.2f}."

    if "average payout" in question and "car" in question:

        avg = car_claims["claim_amount"].mean()

        return f"The average payout for car claims is ₹{avg:,.2f}."

    if "approval rate" in question:

        rate = all_claims["claim_approved"].mean() * 100

        return f"The overall claim approval rate is {rate:.2f}%."

    if "approval probability below 40" in question:

        risky = all_claims[
            all_claims["approval_probability"] < 0.40
        ]

        return (
            f"There are {len(risky):,} claims with approval probability below 40%. "
            "These should be flagged for human review."
        )

    if "top cities" in question or "most claims" in question:

        top_cities = (
            all_claims["city"]
            .value_counts()
            .head(5)
        )

        answer = "Top 5 cities by claim volume:\n"

        for city, count in top_cities.items():
            answer += f"- {city}: {count:,} claims\n"

        return answer

    if "vehicle model" in question and "most claims" in question:

        top_model = (
            all_claims["vehicle_model"]
            .value_counts()
            .idxmax()
        )

        count = (
            all_claims["vehicle_model"]
            .value_counts()
            .max()
        )

        return (
            f"The vehicle model with the most claims is {top_model} "
            f"with {count:,} claims."
        )

    if "how many quotations" in question or "total quotations" in question:

        total = len(all_quotes)

        return f"The total number of quotations generated is {total:,}."

    if "average premium" in question:

        avg = all_quotes["annual_premium"].mean()

        return f"The average quoted premium is ₹{avg:,.2f}."

    if "electric cars" in question and "quotation" in question:

        electric_cars = car_quotes[
            car_quotes["fuel_type"].str.lower() == "electric"
        ]

        return (
            f"There are {len(electric_cars):,} electric car quotations."
        )

    if "highest average claim" in question or "damage type" in question:

        result = (
            all_claims
            .groupby("damage_type")["claim_amount"]
            .mean()
            .sort_values(ascending=False)
        )

        top_damage = result.index[0]
        amount = result.iloc[0]

        return (
            f"The damage type with the highest average claim amount is "
            f"{top_damage}, with an average payout of ₹{amount:,.2f}."
        )

    return (
        "I can answer questions about claims, premiums, approvals, "
        "top cities, vehicle models, risky claims, and quotation counts."
    )