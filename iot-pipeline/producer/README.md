# Producer

## Overview
This folder contains the Python script responsible for generating simulated IoT sensor data, including temperature and humidity readings. The producer sends these readings to a Kafka topic in real time for further processing.

## Files
- producer.py — Generates and publishes IoT sensor readings.

## Requirements
- Python 3.9+
- Kafka broker running locally (from docker-compose)
- Install dependencies:
  pip install -r ../requirements.txt

## How to Run
python3 producer.py

## Output
Real-time sensor readings are published to the Kafka topic: sensor_data
