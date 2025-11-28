import csv
import random
import time
from datetime import datetime

# File to store sensor data
FILE_PATH = "sensor_log.csv"

def generate_sensor_data():
    return {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "air_quality": random.randint(10, 150)
    }

def write_to_csv():
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        data = generate_sensor_data()
        writer.writerow(data.values())
        print("Generated:", data)

if __name__ == "__main__":
    print("Generating sensor data...")
    while True:
        write_to_csv()
        time.sleep(5)  # Generate every 5 seconds
