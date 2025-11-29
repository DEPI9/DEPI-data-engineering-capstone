import json
import pyodbc
from datetime import datetime
from kafka import KafkaConsumer

# ------------------------------------------
# 1. الاتصال بـ Azure SQL
# ------------------------------------------
try:
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
    cursor = conn.cursor()
    print("✅ Connected to Azure SQL successfully")
except Exception as e:
    print("❌ Failed to connect to Azure SQL:", e)
    exit(1)

# ملاحظة: الجداول المفروض تكون متكوّنة مسبقاً في Azure SQL:
# dbo.SensorReadings (id, device_id, temperature, humidity, ts)
# dbo.SensorAlerts   (alert_id, device_id, ts, alert_type, value)

# ------------------------------------------
# 2. Kafka Consumer
# ------------------------------------------
consumer = KafkaConsumer(
    "iot-stream",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("📥 Kafka Consumer is running… Waiting for messages...\n")

# ------------------------------------------
# 3. معالجة كل رسالة قادمة
# ------------------------------------------
for msg in consumer:
    try:
        data = msg.value
        device_id = "device_1"
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ✅ إدخال قراءة الحساس في SensorReadings دائماً
        cursor.execute(
            """
            INSERT INTO dbo.SensorReadings (device_id, temperature, humidity, ts)
            VALUES (?, ?, ?, ?)
            """,
            (device_id, data["temperature"], data["humidity"], data["timestamp"])
        )

        alerts = []

        # 🔺 تنبيه درجة حرارة عالية
        if data["temperature"] > 35:
            alerts.append(f"High Temperature: {data['temperature']}")
            cursor.execute(
                """
                INSERT INTO dbo.SensorAlerts (device_id, ts, alert_type, value)
                VALUES (?, ?, ?, ?)
                """,
                (device_id, data["timestamp"], "High Temperature", data["temperature"])
            )

        # 🔻 تنبيه رطوبة منخفضة
        if data["humidity"] < 10:
            alerts.append(f"Low Humidity: {data['humidity']}")
            cursor.execute(
                """
                INSERT INTO dbo.SensorAlerts (device_id, ts, alert_type, value)
                VALUES (?, ?, ?, ?)
                """,
                (device_id, data["timestamp"], "Low Humidity", data["humidity"])
            )

        # حفظ كل التغييرات
        conn.commit()

        # طباعة في الـ terminal
        if alerts:
            print(
                f"[{now}] Device: {device_id} | "
                f"Temp: {data['temperature']}°C | "
                f"Hum: {data['humidity']}% | "
                f"🚨 ALERTS: {' | '.join(alerts)}\n"
            )
        else:
            print(
                f"[{now}] Device: {device_id} | "
                f"Temp: {data['temperature']}°C | "
                f"Hum: {data['humidity']}% | "
                f"✅ No alerts\n"
            )

    except Exception as e:
        print("❌ Error inserting record:", e)
        conn.rollback()

