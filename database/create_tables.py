from database.db import engine
from database.db import Base
from database import models

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")