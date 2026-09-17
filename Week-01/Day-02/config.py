import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI User Processor")
DEFAULT_ROLE = os.getenv("DEFAULT_ROLE", "Student")

try:
    MAX_USERS = int(os.getenv("MAX_USERS", "10"))
except ValueError:
    MAX_USERS = 10