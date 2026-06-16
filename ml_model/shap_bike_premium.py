import pandas as pd
import pickle
import os
import shap
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(__file__)

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "quotation_data",
    "acko_bike_quotation.csv"
)

model_path = os.path.join(
    BASE_DIR,
    "bike_premium_model.pkl"
)

df = pd.read_csv(csv_path)

features = [
    "customer_age",
    "city_risk_score",
    "vehicle_age_years",
    "engine_cc",
    "idv",
    "ncb_percent",
    "claim_history_count",
    "num_addons"
]

X = df[features]

with open(model_path, "rb") as f:
    model = pickle.load(f)

sample_X = X.sample(
    100,
    random_state=42
)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(sample_X)

output_dir = os.path.join(
    BASE_DIR,
    "..",
    "reports",
    "shap"
)

os.makedirs(
    output_dir,
    exist_ok=True
)

shap.summary_plot(
    shap_values,
    sample_X,
    show=False
)

plt.tight_layout()

output_path = os.path.join(
    output_dir,
    "bike_premium_shap_summary.png"
)

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Bike premium SHAP plot saved at:",
    output_path
)