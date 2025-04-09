from dotenv import load_dotenv
import os

# receive data from .env
load_dotenv()

TOKEN = os.environ.get("TOKEN")
