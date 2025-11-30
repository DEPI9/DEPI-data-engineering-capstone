# Kafka Setup

## Overview
This folder contains the Docker Compose configuration needed to run Kafka and Zookeeper locally. Kafka acts as the message broker for the IoT streaming pipeline.

## Files
- docker-compose.yml — Defines Kafka & Zookeeper services.

## Requirements
- Docker & Docker Compose installed

## Start Kafka
docker compose up -d

## Stop Kafka
docker compose down

## Notes
- Kafka runs on port 9092
- Zookeeper runs on port 2181

