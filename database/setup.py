from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url)

try:
    with engine.connect() as connection:
        print("Connected to PostgreSQL database successfully!")
except Exception as e:
    print(f"Error: {e}")