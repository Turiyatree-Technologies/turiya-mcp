import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Export them for use in other files
FRAPPE_URL = os.getenv("FRAPPE_URL")
API_KEY = os.getenv("API_KEY")

if not FRAPPE_URL or not API_KEY:
    raise ValueError("Missing FRAPPE_URL or API_KEY in .env file")