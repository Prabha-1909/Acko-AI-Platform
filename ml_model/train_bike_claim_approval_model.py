import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report
)

BASE_DIR = os.path.dirname(__file__)

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "claims_data",
    "acko_bike_claims.csv"
)

df = pd.read_csv(csv_path)

X = df[
    [
        "damage_severity_score",
        "num_parts_affected",
        "vehicle_age_years",
        "idv",
        "city_risk_score",
        "previous_claims_count",
        "policy_age_months"
    ]
]

y = df["claim_approved"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)
roc_auc = roc_auc_score(y_test, probabilities)

print("Accuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))
print("ROC-AUC  :", round(roc_auc, 4))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

model_path = os.path.join(
    BASE_DIR,
    "bike_claim_approval_model.pkl"
)

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("Bike Claim Approval Model Saved")