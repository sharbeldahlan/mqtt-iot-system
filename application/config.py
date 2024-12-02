import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    # Flask Settings
    SECRET_KEY = os.getenv("SECRET_KEY")
