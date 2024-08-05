from dotenv import load_dotenv
import os
import pandas as pd
import sqlalchemy as db
import urllib
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
# Convert to sql alchemy for nice print out
connection_uri = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(conn_str)}"


# Establish the connection
engine = db.create_engine(connection_uri)

# Sample query
query = 'SELECT * FROM  ReportTreeNodes'

# Read in the data frame and print out to console
df = pd.read_sql(query, engine)
print(df)
