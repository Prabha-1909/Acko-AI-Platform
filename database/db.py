from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = (
    "postgresql://postgres:Prabha_1909"
    "@acko-ai-db.cp22wcquc88h.ap-south-1.rds.amazonaws.com:5432/postgres"
    "?sslmode=require"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()