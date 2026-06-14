from database.db import SessionLocal
from database.models import ChatLog
from database.models import Quotation
from database.models import Claim


def save_chat_log(
    question,
    response,
    intent="policy_qa",
    user_id=None,
    retrieved_source=None
):

    db = SessionLocal()

    try:
        log = ChatLog(
            user_id=user_id,
            intent=intent,
            question=question,
            response=response,
            retrieved_source=retrieved_source
        )

        db.add(log)
        db.commit()

    finally:
        db.close()


def save_quotation(
    vehicle_type,
    predicted_premium,
    user_id=None,
    vehicle_make=None,
    vehicle_model=None,
    manufacturing_year=None,
    city=None,
    idv=None,
    ncb_percent=None
):

    db = SessionLocal()

    try:
        quotation = Quotation(
            user_id=user_id,
            vehicle_type=vehicle_type,
            vehicle_make=vehicle_make,
            vehicle_model=vehicle_model,
            manufacturing_year=manufacturing_year,
            city=city,
            idv=idv,
            ncb_percent=ncb_percent,
            predicted_premium=predicted_premium
        )

        db.add(quotation)
        db.commit()

    finally:
        db.close()


def save_claim(
    vehicle_type,
    damage_type,
    affected_parts,
    damage_severity,
    predicted_amount,
    approval_probability,
    status,
    user_id=None,
    policy_number=None,
    incident_date=None,
    image_s3_key=None,
    form_s3_key=None
):

    db = SessionLocal()

    try:
        claim = Claim(
            user_id=user_id,
            vehicle_type=vehicle_type,
            policy_number=policy_number,
            incident_date=incident_date,
            damage_type=damage_type,
            affected_parts=affected_parts,
            damage_severity=damage_severity,
            image_s3_key=image_s3_key,
            form_s3_key=form_s3_key,
            predicted_amount=predicted_amount,
            approval_probability=approval_probability,
            status=status
        )

        db.add(claim)
        db.commit()

    finally:
        db.close()