import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

# إعداد Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def generate_sensor_data():
    """توليد بيانات حساس وهمية"""
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(20, 40), 2),  # بين 20 و 40
        "humidity": round(random.uniform(5, 30), 2),      # بين 5 و 30
        "air_quality": random.randint(10, 150)            # قيمة جودة هواء عشوائية
    }

print("🚀 Kafka Producer started. Sending data every 5 seconds...")

while True:
    data = generate_sensor_data()
    producer.send("iot-stream", data)
    print("Sent:", data)
    time.sleep(5)

