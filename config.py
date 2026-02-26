import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API = os.getenv("OPENAI_API")
MODEL_NAME = "gpt-4o-mini"
