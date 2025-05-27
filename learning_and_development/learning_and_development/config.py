import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
load_dotenv(dotenv_path, override=True)  # <--- force override

DJANGO_ENV = os.getenv("DJANGO_ENV", "development")
USER_API_URL = os.getenv("USER_API_URL", "http://127.0.0.1:8000")
COURSE_API_URL = os.getenv("COURSE_API_URL", "http://127.0.0.1:8000")
RUN_LOCAL = os.getenv("RUN_LOCAL", "false").lower() == "true"

