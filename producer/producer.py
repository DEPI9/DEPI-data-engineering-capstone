from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


print("📤 Kafka Producer started...")

while True:
    data = {
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 60), 2)
    }

    producer.send("iot-data", data)
    print("Sent:", data)

    time.sleep(5)
