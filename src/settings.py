# src/settings.py
import os
from dotenv import load_dotenv

# Find the .env file (it's one level up from this file's directory)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Now, load those variables from the environment
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "dbname": os.getenv("DB_NAME")
}

SCRAPER_CONFIG = {
    "base_url": os.getenv("VLR_BASE_URL"),
    "rate_limit_delay": int(os.getenv("RATE_LIMIT_DELAY", 3)) # Default to 3
}

# Check if a critical variable is missing
if not DB_CONFIG["password"]:
    raise ValueError("Error: DB_PASSWORD not found. Did you create your .env file?")