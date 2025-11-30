# Generator

## Overview
This folder includes the script responsible for generating raw IoT sensor data and saving it to a CSV file. It is mainly used for batch ETL processing and offline testing.

## Files
- generator.py — Creates synthetic temperature and humidity readings.
- sensor_log.csv — Sample generated data.

## How to Run
python3 generator.py

## Output
A CSV file named sensor_log.csv containing:
- timestamp
- temperature
- humidity

