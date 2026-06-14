import streamlit as st

def show_kpis(
    bike_quotes,
    car_quotes,
    health_quotes,
    bike_claims,
    car_claims
):

    total_claims = (
        len(bike_claims)
        + len(car_claims)
    )

    avg_bike_claim = round(
        bike_claims["claim_amount"].mean(),
        2
    )

    avg_car_claim = round(
        car_claims["claim_amount"].mean(),
        2
    )

    approval_rate = round(

        (
            bike_claims["claim_approved"].mean()
            +
            car_claims["claim_approved"].mean()
        )
        / 2
        * 100,

        2
    )

    total_quotes = (
        len(bike_quotes)
        + len(car_quotes)
        + len(health_quotes)
    )

    avg_premium = round(

        (
            bike_quotes["annual_premium"].mean()
            +
            car_quotes["annual_premium"].mean()
            +
            health_quotes["annual_premium"].mean()
        ) / 3,

        2
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Claims",
        f"{total_claims:,}"
    )

    col2.metric(
        "Bike Avg Claim",
        f"₹{avg_bike_claim:,.0f}"
    )

    col3.metric(
        "Car Avg Claim",
        f"₹{avg_car_claim:,.0f}"
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Approval Rate",
        f"{approval_rate}%"
    )

    col5.metric(
        "Total Quotations",
        f"{total_quotes:,}"
    )

    col6.metric(
        "Avg Premium",
        f"₹{avg_premium:,.0f}"
    )