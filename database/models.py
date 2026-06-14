from sqlalchemy import Column, String, Integer, Float, DateTime, Text
from datetime import datetime
import uuid

from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100))
    email = Column(String(150))
    phone = Column(String(15))
    role = Column(String(20), default="customer")
    created_at = Column(DateTime, default=datetime.utcnow)


class Quotation(Base):
    __tablename__ = "quotations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)
    vehicle_type = Column(String(10))
    vehicle_make = Column(String(50))
    vehicle_model = Column(String(80))
    manufacturing_year = Column(Integer)
    city = Column(String(80))
    idv = Column(Float)
    ncb_percent = Column(Integer)
    predicted_premium = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


class Claim(Base):
    __tablename__ = "claims"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)
    vehicle_type = Column(String(10))
    policy_number = Column(String(50))
    incident_date = Column(String)
    damage_type = Column(String(50))
    affected_parts = Column(String(200))
    damage_severity = Column(String(20))
    image_s3_key = Column(String(255))
    form_s3_key = Column(String(255))
    predicted_amount = Column(Float)
    approval_probability = Column(Float)
    status = Column(String(20), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)


class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)
    intent = Column(String(30))
    question = Column(Text)
    retrieved_source = Column(String(255))
    response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)