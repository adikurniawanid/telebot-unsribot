from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

API_URL = os.getenv("API_URL")
TOKEN_TELEBOT = os.getenv("TOKEN_TELEBOT")
