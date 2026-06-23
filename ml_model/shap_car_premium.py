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
    "acko_car_quotation.csv"
)

model_path = os.path.join(
    BASE_DIR,
    "car_premium_model.pkl"
)

output_path = os.path.join(
    BASE_DIR,
    "car_premium_shap.png"
)

df = pd.read_csv(csv_path)

with open(model_path, "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]
feature_columns = model_data["feature_columns"]

df = pd.get_dummies(
    df,
    columns=[
        "segment",
        "fuel_type",
        "policy_type"
    ]
)

for col in feature_columns:
    if col not in df.columns:
        df[col] = 0

X = df[feature_columns]

sample_X = X.sample(
    n=min(100, len(X)),
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