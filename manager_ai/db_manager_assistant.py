import pandas as pd

from database.db import engine


def load_db_tables():

    quotations = pd.read_sql(
        "SELECT * FROM quotations",
        engine
    )

    claims = pd.read_sql(
        "SELECT * FROM claims",
        engine
    )

    chat_logs = pd.read_sql(
        "SELECT * FROM chat_logs",
        engine
    )

    return quotations, claims, chat_logs


def ask_db_manager(question):

    question = question.lower()

    quotations, claims, chat_logs = load_db_tables()

    if "how many quotations" in question or "total quotations" in question:

        return f"Total quotations generated: {len(quotations)}"

    if "average premium" in question:

        avg = quotations["predicted_premium"].mean()

        return f"Average predicted premium: ₹{avg:,.2f}"

    if "how many claims" in question or "total claims" in question:

        return f"Total claims submitted: {len(claims)}"

    if "approved claims" in question:

        approved = claims[
            claims["status"] == "approved"
        ]

        return f"Approved claims count: {len(approved)}"

    if "manual review" in question or "review claims" in question:

        review = claims[
            claims["status"] == "review"
        ]

        return f"Claims flagged for manual review: {len(review)}"

    if "chat" in question or "questions" in question:

        return f"Total chatbot conversations logged: {len(chat_logs)}"

    if "highest premium" in question:

        max_row = quotations.sort_values(
            "predicted_premium",
            ascending=False
        ).iloc[0]

        return (
            f"Highest premium is ₹{max_row['predicted_premium']:,.2f} "
            f"for {max_row['vehicle_type']} insurance."
        )

    if "latest claim" in question:

        latest = claims.sort_values(
            "created_at",
            ascending=False
        ).iloc[0]

        return (
            f"Latest claim is for {latest['vehicle_type']} insurance, "
            f"amount ₹{latest['predicted_amount']:,.2f}, "
            f"status {latest['status']}."
        )

    return (
        "I can answer database questions about quotations, premiums, "
        "claims, approval status, manual review, and chatbot logs."
    )