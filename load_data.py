import pandas as pd
import pyodbc

# ───────────────────────────────────────────────────────────────
# 1.  Load the CSV  (adjust nrows or filename if you like)
# ───────────────────────────────────────────────────────────────
df = pd.read_csv("data/yellow_tripdata.csv", nrows=100_000)

# Keep only the columns you need and rename them to match the SQL table
df = df[
    [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "PULocationID",
        "DOLocationID",
        "passenger_count",
        "trip_distance",
        "fare_amount",
        "tip_amount",
        "total_amount",
        "payment_type",
    ]
]

df.columns = [
    "pickup_datetime",
    "dropoff_datetime",
    "pickup_location_id",
    "dropoff_location_id",
    "passenger_count",
    "trip_distance",
    "fare_amount",
    "tip_amount",
    "total_amount",
    "payment_type",
]

# ───────────────────────────────────────────────────────────────
# 2.  Connect to SQL Server  (Windows Authentication)
#    – For Driver 17  (use this if 18 is not installed)
# ───────────────────────────────────────────────────────────────
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"   # ← exactly what SSMS shows
    "DATABASE=CabDB;"
    "Trusted_Connection=yes;"         # ← uses LAPTOP-8KA6T75U\\gunas
)

# ──  If you have ODBC Driver 18 installed, comment out the block above
#     and use this instead (required because Driver 18 defaults to TLS):
# conn = pyodbc.connect(
#     "DRIVER={ODBC Driver 18 for SQL Server};"
#     "SERVER=localhost\\SQLEXPRESS;"
#     "DATABASE=CabDB;"
#     "Trusted_Connection=yes;"
#     "Encrypt=no;"
#     "TrustServerCertificate=yes;"
# )

cursor = conn.cursor()

# ───────────────────────────────────────────────────────────────
# 3.  Insert rows into the table
# ───────────────────────────────────────────────────────────────
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO CabTrips (
            pickup_datetime,
            dropoff_datetime,
            pickup_location_id,
            dropoff_location_id,
            passenger_count,
            trip_distance,
            fare_amount,
            tip_amount,
            total_amount,
            payment_type
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        tuple(row),
    )

conn.commit()
cursor.close()
conn.close()

print("Data loaded successfully.")
