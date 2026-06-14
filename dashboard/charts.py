import streamlit as st
import plotly.express as px
import pandas as pd


def show_charts(
    bike_quotes,
    car_quotes,
    health_quotes,
    bike_claims,
    car_claims
):

    st.subheader("📈 Insurance Analytics")

    # =====================
    # Claim Volume by City
    # =====================

    all_claims = pd.concat(
        [bike_claims, car_claims],
        ignore_index=True
    )

    damage_claims = (
    all_claims
    .groupby("damage_type")["claim_amount"]
    .mean()
    .reset_index(name="avg_claim_amount")
    .sort_values(
        "avg_claim_amount",
        ascending=False
    )
)

    fig1 = px.bar(
    damage_claims,
    x="damage_type",
    y="avg_claim_amount",
    title="Average Claim Amount by Damage Type"
)

    st.plotly_chart(
    fig1,
    use_container_width=True
)

    # =====================
    # Claim Approval
    # =====================

    approval_counts = (
        all_claims["claim_approved"]
        .value_counts()
        .reset_index()
    )

    approval_counts.columns = [
        "Status",
        "Count"
    ]

    approval_counts["Status"] = (
        approval_counts["Status"]
        .map({
            1: "Approved",
            0: "Rejected"
        })
    )

    fig2 = px.pie(
        approval_counts,
        names="Status",
        values="Count",
        title="Claim Approval Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # =====================
    # Premium Distribution
    # =====================

    premium_data = pd.DataFrame({

        "Insurance Type": [

            "Bike",
            "Car",
            "Health"

        ],

        "Average Premium": [

            bike_quotes["annual_premium"].mean(),

            car_quotes["annual_premium"].mean(),

            health_quotes["annual_premium"].mean()

        ]
    })

    fig3 = px.bar(
        premium_data,
        x="Insurance Type",
        y="Average Premium",
        title="Average Premium by Insurance Type"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    severity_claims = (
    all_claims
    .groupby("damage_severity_score")["claim_amount"]
    .mean()
    .reset_index()
)

    fig = px.line(
        severity_claims,
        x="damage_severity_score",
        y="claim_amount",
        markers=True,
        title="Damage Severity vs Average Claim Amount"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================
# Manual Review Queue
# =====================

    st.subheader(
        "🚨 Claims Flagged For Manual Review"
    )

    review_claims = all_claims[
        all_claims["approval_probability"] < 0.50
    ]

    st.dataframe(
        review_claims[
            [
                "record_id",
                "city",
                "damage_type",
                "claim_amount",
                "approval_probability"
            ]
        ].head(20)
    )