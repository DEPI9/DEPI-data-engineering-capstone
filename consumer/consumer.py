from kafka import KafkaConsumer
import json
import pyodbc

# ---------------------------
# Azure SQL Connection
# ---------------------------
conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:iotpipelineserver.database.windows.net,1433;"
    "Database=iotdb;"
    "Uid=depiadmin;"
    "Pwd=depi@999;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# إنشاء الجدول إذا مش موجود
cursor.execute("""
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='iot_data' AND xtype='U')
CREATE TABLE iot_data (
    id INT IDENTITY(1,1) PRIMARY KEY,
    temperature FLOAT,
    humidity FLOAT,
    created_at DATETIME DEFAULT GETDATE()
)
""")
conn.commit()

# ---------------------------
# Kafka Consumer
# ---------------------------
consumer = KafkaConsumer(
    "iot-data",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)


print("📥 Kafka Consumer started. Waiting for messages...")

for msg in consumer:
    data = msg.value
    print("Received:", data)

    temp = data["temperature"]
    hum = data["humidity"]

    cursor.execute(
        "INSERT INTO iot_data (temperature, humidity) VALUES (?, ?)",
        (temp, hum)
    )
    conn.commit()

    print("✔ Inserted into Azure SQL")
