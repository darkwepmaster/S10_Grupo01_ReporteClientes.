import pyodbc
from config import DB_SERVER, DB_PORT, DB_DATABASE, DB_USER, DB_PASSWORD


def get_connection():
    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={DB_SERVER},{DB_PORT};"
        f"DATABASE={DB_DATABASE};"
        f"UID={DB_USER};PWD={DB_PASSWORD};"
        "Encrypt=yes;TrustServerCertificate=yes;"
    )
    return pyodbc.connect(connection_string)
