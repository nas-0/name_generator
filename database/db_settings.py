from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db_url = os.getenv("DATABASE_URL")