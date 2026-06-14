import pickle
import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)

with open(
    os.path.join(BASE_DIR, "health_premium_model.pkl"),
    "rb"
) as f:
    model = pickle.load(f)

def predict_health_premium(
    age,
    gender,
    num_members,
    city_tier,
    bmi_category,
    smoke,
    has_pre_existing,
    ncb_years,
    sum_insured,
    deductible,
    num_addons,
    has_maternity,
    has_opd,
    policy_tenure
):

    data = pd.DataFrame([[
        age,
        gender,
        num_members,
        city_tier,
        bmi_category,
        smoke,
        has_pre_existing,
        ncb_years,
        sum_insured,
        deductible,
        num_addons,
        has_maternity,
        has_opd,
        policy_tenure
    ]], columns=[

        "age",
        "gender",
        "num_members",
        "city_tier",
        "bmi_category",
        "smoke",
        "has_pre_existing",
        "ncb_years",
        "sum_insured",
        "deductible",
        "num_addons",
        "has_maternity",
        "has_opd",
        "policy_tenure"

    ])

    premium = model.predict(data)[0]

    return {
        "predicted_premium": round(float(premium), 2)
    }