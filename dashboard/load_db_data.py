import pandas as pd
from database.db import engine


def load_db_data():

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