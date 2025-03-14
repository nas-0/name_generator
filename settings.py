from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_url = os.getenv("DEEPSEEK_URL")
db_url = os.getenv("DATABASE_URL")