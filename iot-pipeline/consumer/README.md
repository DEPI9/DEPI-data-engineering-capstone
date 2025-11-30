# Consumer

## Overview
This module listens to the Kafka topic that receives IoT sensor readings. It processes each message, checks for anomalies, and prints alerts if temperature or humidity exceed defined thresholds.

## Files
- consumer.py — Reads messages from Kafka and applies alert logic.

## Requirements
- Python 3.9+
- Kafka broker running
- Install dependencies:
  pip install -r ../requirements.txt

## How to Run
python3 consumer.py

## Output
- Normal readings printed to console
- Alerts printed when values exceed thresholds

