import os
from dotenv import load_dotenv

# Load environment variables from .env file once
load_dotenv()

DJANGO_ENV = os.getenv("DJANGO_ENV", "development")
USER_API_URL = os.getenv("USER_API_URL", "http://127.0.0.1:8000")
COURSE_API_URL = os.getenv("COURSE_API_URL", "http://127.0.0.1:8000")
RUN_LOCAL = os.getenv("RUN_LOCAL", "false").lower() == "true"
