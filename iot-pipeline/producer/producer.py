import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_sensor_data():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "air_quality": random.randint(10, 150)
    }

print("🚀 Kafka Producer started. Sending data every 5 seconds...")

while True:
    data = generate_sensor_data()
    producer.send("iot-stream", data)
    print("Sent:", data)
    time.sleep(5)
