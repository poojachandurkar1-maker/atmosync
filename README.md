*# AtmoSync IoT – Real-Time Micro-Climate Monitoring Pipeline*



*## Project Overview*



*AtmoSync IoT is a real-time IoT data engineering project designed to monitor*

*micro-climate conditions inside shipping containers.*



*The system collects temperature and humidity telemetry from simulated IoT*

*sensors, streams the data through Apache Kafka, processes the telemetry, and*

*stores it for analytics and dashboard visualization.*



*## Problem Statement*



*Traditional supply-chain monitoring often depends on external weather data.*

*However, conditions inside a shipping container can change significantly.*



*AtmoSync monitors:*



*- Container temperature*

*- Container humidity*

*- Container ID*

*- Container location*

*- Sensor timestamp*



*The system identifies containers where environmental conditions exceed*

*commodity safety thresholds.*



*## Architecture*



*IoT Sensor Simulator*

&#x20;       *|*

&#x20;       *v*

*Apache Kafka*

&#x20;       *|*

&#x20;       *v*

*Kafka Consumer*

&#x20;       *|*

&#x20;       *v*

*PostgreSQL*

&#x20;       *|*

&#x20;       *v*

*Analytics / Refresh Pipeline*

&#x20;       *|*

&#x20;       *v*

*Power BI Dashboard*

&#x20;       *|*

&#x20;       *v*

*Risk Monitoring \& Alerts*



*## Technologies*



*- Python*

*- Apache Kafka*

*- PostgreSQL*

*- SQL*

*- Power BI*

*- Git \& GitHub*



*## Main Components*



*### IoT Simulator*



*Generates simulated container telemetry including temperature, humidity,*

*location, timestamp, and container ID.*



*### Kafka Producer*



*Publishes sensor telemetry to Kafka topics.*



*### Kafka Consumer*



*Consumes telemetry messages from Kafka for downstream processing.*



*### PostgreSQL*



*Stores sensor and analytics data.*



*### Refresh Pipeline*



*Processes and refreshes telemetry data for analytics.*



*### Email Alerts*



*Generates alerts when containers become high-risk.*



*## Project Goal*



*The goal of AtmoSync IoT is to create an automated streaming pipeline capable*

*of detecting environmental risks in shipping containers and supporting*

*real-time supply-chain decisions.*





