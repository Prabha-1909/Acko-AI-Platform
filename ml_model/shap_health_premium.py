import os
import pickle
import pandas as pd
import shap
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(__file__)

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "quotation_data",
    "acko_health_quotation.csv"
)

model_path = os.path.join(
    BASE_DIR,
    "health_premium_model.pkl"
)

output_path = os.path.join(
    BASE_DIR,
    "health_premium_shap.png"
)

df = pd.read_csv(csv_path)

feature_columns = [
    "age",
    "num_members",
    "city_tier",
    "has_pre_existing",
    "annual_checkup",
    "ncb_years",
    "sum_insured",
    "deductible",
    "num_addons",
    "has_maternity",
    "has_opd",
    "policy_tenure"
]

X = df[feature_columns]

with open(model_path, "rb") as f:
    model = pickle.load(f)

sample_X = X.sample(
    n=min(200, len(X)),
    random_state=42
)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(
    sample_X,
    check_additivity=False
)

plt.figure()

shap.summary_plot(
    shap_values,
    sample_X,
    show=False
)

plt.tight_layout()

plt.savefig(
    output_path,
    bbox_inches="tight"
)

print("SHAP plot saved at:", output_path)