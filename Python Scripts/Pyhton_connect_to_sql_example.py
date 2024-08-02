from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

# Create the connection string
conn_str = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    f'SERVER={os.getenv("LOCAL_DB_SERVER")};'
    f'DATABASE={os.getenv("LOCAL_DB")};'
    f'UID={os.getenv("LOCAL_DB_USERNAME")};'
    f'PWD={os.getenv("LOCAL_DB_PASSWORD")};'
    'TrustServerCertificate=yes;'
    'Encrypt=yes;'
)

query = f"""
SELECT * FROM ReportTreeNodes
"""



# Establish the connection
try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful!")
    cursor = conn.cursor()
    cursor.execute(query)
    fks = cursor.fetchall()
    print(fks)
except Exception as e:
    print(f"Error: {e}")
