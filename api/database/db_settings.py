from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url)