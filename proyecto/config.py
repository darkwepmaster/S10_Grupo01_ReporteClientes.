"""Configuración central: lee variables de entorno (.env). Nunca se escriben secretos en el código."""
from dotenv import load_dotenv
import os

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_PORT = os.getenv("DB_PORT", "1433")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

if not all([DB_SERVER, DB_DATABASE, DB_USER, DB_PASSWORD]):
    raise RuntimeError("Faltan variables de entorno obligatorias (revise .env)")
