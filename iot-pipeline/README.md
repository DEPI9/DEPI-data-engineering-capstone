# IoT Data Pipeline – DEPI Data Engineering Capstone

## Overview
This project implements a complete real-time IoT data pipeline that simulates temperature and humidity readings, streams them through Kafka, processes the data using Python, stores the results in Azure SQL Database, and visualizes insights using a Power BI dashboard. The pipeline showcases modern data engineering concepts such as data simulation, ETL, streaming, alert detection, cloud storage, and reporting.

## Architecture
1. Data Generator – Generates synthetic IoT sensor readings and saves raw CSV files.
2. Batch ETL – Cleans and transforms raw sensor data into a structured dataset.
3. Kafka Producer – Sends real-time sensor data to the Kafka topic “sensor_data”.
4. Kafka Consumer – Processes incoming data, checks thresholds, and prints alerts.
5. Azure SQL Database – Stores processed readings for analytics.  
   ⚠️ Note: Azure SQL cannot be accessed externally due to firewall restrictions.
6. Power BI Dashboard – Visualizes trends, KPIs, and alert statistics.

## Folder Structure
iot-pipeline/  
│  
├── generator/      # Raw data generator  
├── etl/            # Batch ETL processing  
├── producer/       # Kafka producer  
├── consumer/       # Kafka consumer  
├── kafka/          # Docker Compose (Kafka + Zookeeper)  
├── streaming/      # Streaming dependencies  
└── dashboard/      # Power BI dashboard files

## How the Pipeline Works
1. Start Kafka using Docker:  
   docker compose up -d  
2. Run the Producer to send live IoT data:  
   python3 producer/producer.py  
3. Run the Consumer to process readings:  
   python3 consumer/consumer.py  
4. (Optional) Run the ETL script for batch cleaning:  
   python3 etl/batch_etl.py  
5. Load the processed data into Azure SQL.  
   ⚠️ Direct access from outside Azure is blocked due to firewall rules.  
6. Refresh the Power BI dashboard to view:  
   - Temperature trend  
   - Humidity trend  
   - Alerts  
   - KPIs  
   - Normal vs abnormal distribution

## Key Features
- Real-time IoT data streaming  
- Kafka-based messaging architecture  
- Python processing & anomaly detection  
- Azure SQL cloud storage  
- Power BI analytics dashboard  
- Clean modular folder structure

## Technologies Used
Python 3.9+  
Apache Kafka  
Docker Compose  
Azure SQL Database  
Power BI  
Pandas / Logging / JSON

## Notes
- This project follows DEPI Data Engineering Capstone requirements.  
- Azure SQL access is limited because of firewall restrictions.  
- All modules can run independently for testing.

## Team Members
Data Simulation  
ETL / Cleaning  
Streaming Logic  
SQL Development  
Dashboard Development  
Documentation & Presentation

