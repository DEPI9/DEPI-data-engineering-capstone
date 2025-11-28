import json
from kafka import KafkaConsumer
import pyodbc

# ------------------------------------------
# 1. Connect to Azure SQL
# ------------------------------------------
conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=iot-depi-sql-server.database.windows.net;"
    "Database=iotdb;"
    "UID=adminuser;"
    "PWD=depi@9999;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

print("Connected!")


cursor = conn.cursor()

print("📡 Connected to Azure SQL successfully")

# ------------------------------------------
# 2. Kafka Consumer
# ------------------------------------------
consumer = KafkaConsumer(
    "iot-stream",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("📥 Awaiting messages...")

# ------------------------------------------
# 3. Insert rows into Azure SQL
# ------------------------------------------
for msg in consumer:
    data = msg.value

    print("➡️ Received:", data)

    cursor.execute("""
        INSERT INTO sensor_data (timestamp, temperature, humidity, air_quality)
        VALUES (?, ?, ?, ?)
    """, data["timestamp"], data["temperature"], data["humidity"], data["air_quality"])

    conn.commit()
    print("✔ Data inserted into Azure SQL!")
