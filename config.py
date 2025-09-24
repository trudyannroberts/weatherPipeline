import os
from pathlib import Path
from dotenv import load_dotenv

# Finn alltid .env relativt til prosjektroten
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# API
CLIENT_ID = os.getenv("FROST_CLIENT_ID")
PASSWORD = os.getenv("FROST_PASSWORD")

# Database
DB_NAME = os.getenv("DB_NAME", "weatherdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", 'JegLikerKoding10%')
DB_HOST = os.getenv("DB_HOST", "localhost")