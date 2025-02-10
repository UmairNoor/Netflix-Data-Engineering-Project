import pandas as pd
import sqlalchemy as sal
import pyodbc

# Load the CSV file
df = pd.read_csv(r"C:\Users\Umair Noor\Downloads\netflix_titles.csv")

# Define the correct SQLAlchemy engine string
server = "DESKTOP-KIO4BC5\\SQLEXPRESS"  # Your SQL Server Name
database = "AshrafData"  # Change this to your actual database
driver = "ODBC Driver 17 for SQL Server"

# Create the connection string
engine = sal.create_engine(f"mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver={driver}", fast_executemany=True)

# Connect to SQL Server
conn = engine.connect()

# Push DataFrame to SQL Server
df.to_sql('netflix_raw', con=conn, index=False, if_exists='replace')

# Close the connection
conn.close()


df.head()
df[df.show_id=='s5023']
max(df.description.dropna().str.len())
df.isna().sum()
