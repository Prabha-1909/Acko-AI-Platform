from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify



import os
import sys

from werkzeug.utils import secure_filename

print("=" * 50)
print("RUNNING APP FROM:")
print(os.path.abspath(__file__))
print("=" * 50)

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
from storage.s3_uploader import upload_file_to_s3

from rag_chatbot.rag_pipeline import ask_question

from ml_model.bike_premium_predict import predict_bike_premium
from ml_model.car_premium_predict import predict_car_premium
from ml_model.health_premium_predict import predict_health_premium

from claim_ai.damage_analyzer import analyze_damage_image
from ml_model.bike_claim_predict import predict_bike_claim
from ml_model.car_claim_predict import predict_car_claim

from database.crud import save_chat_log
from database.crud import save_quotation
from database.crud import save_claim

# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)

# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# Chatbot API
# ==========================================

@app.route("/ask", methods=["POST"])
def ask():

    print("ASK API HIT")

    data = request.get_json()

    print(data)

    question = data["question"]

    answer = ask_question(question)

    print(answer)

    save_chat_log(
        question=question,
        response=answer,
        intent="policy_qa"
    )

    return jsonify({
        "answer": answer
    })


# ==========================================
# Bike Claim Predictor API
# ==========================================

@app.route("/predict_bike_premium", methods=["POST"])
def predict_bike_premium_route():

    data = request.get_json()

    result = predict_bike_premium(
    customer_age=int(data["customer_age"]),
    city_risk_score=float(data["city_risk_score"]),
    vehicle_age_years=float(data["vehicle_age_years"]),
    engine_cc=float(data["engine_cc"]),
    idv=float(data["idv"]),
    ncb_percent=float(data["ncb_percent"]),
    claim_history_count=int(data["claim_history_count"]),
    num_addons=int(data["num_addons"])
)
    
    save_quotation(
    vehicle_type="bike",
    predicted_premium=result["predicted_premium"],
    city="Unknown",
    idv=float(data["idv"]),
    ncb_percent=int(data["ncb_percent"])
)

    return jsonify(result)


@app.route("/predict_car_premium", methods=["POST"])
def predict_car_premium_route():

    data = request.get_json()

    result = predict_car_premium(
        customer_age=int(data["customer_age"]),
        city_risk_score=float(data["city_risk_score"]),
        vehicle_age_years=float(data["vehicle_age_years"]),
        engine_cc=float(data["engine_cc"]),
        idv=float(data["idv"]),
        ncb_percent=float(data["ncb_percent"]),
        claim_history_count=int(data["claim_history_count"]),
        num_addons=int(data["num_addons"])
    )

    save_quotation(
    vehicle_type="car",
    predicted_premium=result["predicted_premium"],
    city="Unknown",
    idv=float(data["idv"]),
    ncb_percent=int(data["ncb_percent"])
)

    return jsonify(result)

@app.route("/predict_health_premium", methods=["POST"])
def predict_health_premium_route():

    data = request.get_json()

    result = predict_health_premium(

        age=int(data["age"]),
        gender=int(data["gender"]),
        num_members=int(data["num_members"]),
        city_tier=int(data["city_tier"]),
        bmi_category=int(data["bmi_category"]),
        smoke=int(data["smoke"]),
        has_pre_existing=int(data["has_pre_existing"]),
        ncb_years=int(data["ncb_years"]),
        sum_insured=float(data["sum_insured"]),
        deductible=float(data["deductible"]),
        num_addons=int(data["num_addons"]),
        has_maternity=int(data["has_maternity"]),
        has_opd=int(data["has_opd"]),
        policy_tenure=int(data["policy_tenure"])

    )

    save_quotation(
    vehicle_type="health",
    predicted_premium=result["predicted_premium"]
)

    return jsonify(result)

# ==========================================
# Module 3 - Claim Submission API
# ==========================================

@app.route("/submit_claim", methods=["POST"])
def submit_claim():

    vehicle_type = request.form.get("vehicle_type")

    image = request.files.get("damage_image")

    if image is None:
        return jsonify({
            "error": "Damage image is required"
        }), 400

    upload_folder = os.path.join(
        os.path.dirname(__file__),
        "..",
        "uploads",
        "claims"
    )

    os.makedirs(upload_folder, exist_ok=True)

    filename = secure_filename(image.filename)

    image_path = os.path.join(
        upload_folder,
        filename
    )

    image.save(image_path)

    image_s3_key = upload_file_to_s3(
    image_path,
    folder_name="claims/damage_images"
)

    vision_result = analyze_damage_image(image_path)

    damage_severity_score = float(
        vision_result["severity_score"]
    )

    num_parts_affected = int(
        request.form.get("num_parts_affected")
    )

    vehicle_age_years = float(
        request.form.get("vehicle_age_years")
    )

    idv = float(
        request.form.get("idv")
    )

    city_risk_score = float(
        request.form.get("city_risk_score")
    )

    previous_claims_count = int(
        request.form.get("previous_claims_count")
    )

    policy_age_months = int(
        request.form.get("policy_age_months")
    )

    if vehicle_type == "bike":

        prediction = predict_bike_claim(
            damage_severity_score=damage_severity_score,
            num_parts_affected=num_parts_affected,
            vehicle_age_years=vehicle_age_years,
            idv=idv,
            city_risk_score=city_risk_score,
            previous_claims_count=previous_claims_count,
            policy_age_months=policy_age_months
        )

    elif vehicle_type == "car":

        prediction = predict_car_claim(
            damage_severity_score=damage_severity_score,
            num_parts_affected=num_parts_affected,
            vehicle_age_years=vehicle_age_years,
            idv=idv,
            city_risk_score=city_risk_score,
            previous_claims_count=previous_claims_count,
            policy_age_months=policy_age_months
        )

    else:

        return jsonify({
            "error": "Invalid vehicle type"
        }), 400
    claim_status = "pending"

    if prediction["approval_probability"] >= 70:

        claim_status = "approved"

    elif prediction["approval_probability"] < 40:

        claim_status = "review"

    save_claim(
        vehicle_type=vehicle_type,
        damage_type=vision_result["damage_type"],
        affected_parts=vision_result["affected_parts"],
        damage_severity=vision_result["severity"],
        predicted_amount=prediction["predicted_claim_amount"],
        approval_probability=prediction["approval_probability"] / 100,
        status=claim_status,
        image_s3_key=image_s3_key,
        form_s3_key=None
    )
    

    return jsonify({
        "vehicle_type": vehicle_type,
        "damage_type": vision_result["damage_type"],
        "affected_parts": vision_result["affected_parts"],
        "severity": vision_result["severity"],
        "severity_score": vision_result["severity_score"],
        "vision_status": vision_result["vision_status"],
        "predicted_claim_amount": prediction["predicted_claim_amount"],
        "approval_probability": prediction["approval_probability"],
        "image_path": image_path
    })

   


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )