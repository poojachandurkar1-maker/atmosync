# 🌍 AtmoSync - IoT Micro-Climate Arbitrage Analytics


# 📌 Overview

AtmoSync is a real-time IoT analytics platform designed to monitor refrigerated shipping containers and detect spoilage risks using continuous sensor telemetry.

The platform simulates IoT devices, streams telemetry, stores historical data, exposes REST APIs, and supports business dashboards.

---

# 🎯 Business Problem

Agricultural products lose value when temperature and humidity drift outside safe ranges during transportation.

Traditional monitoring systems:

- provide delayed updates
- cannot identify spoilage early
- lack predictive insights

AtmoSync enables continuous monitoring and early intervention.

---

# 💡 Solution

The project provides an end-to-end monitoring pipeline that:

- Simulates IoT sensor data
- Streams telemetry
- Stores readings
- Exposes REST APIs
- Generates alerts
- Supports dashboard visualization

---

# 🏗 System Architecture

```text
                IoT Containers
                      │
                      ▼
         Python IoT Simulator
                      │
                      ▼
               Apache Kafka
                      │
                      ▼
             Kafka Consumer
                      │
                      ▼
              PostgreSQL Database
                      │
                      ▼
             Spring Boot REST API
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
    Power BI Dashboard      Email Alerts
```

---

# ⚙ Technology Stack

### Backend

- Java 21
- Spring Boot
- Spring Data JPA
- Maven

### Programming

- Python

### Database

- PostgreSQL

### Streaming

- Apache Kafka

### Visualization

- Power BI

### DevOps

- Docker
- Docker Compose

### Version Control

- Git
- GitHub

---

# 🚀 Features

✔ IoT Sensor Simulation

✔ Kafka Message Streaming

✔ PostgreSQL Storage

✔ REST APIs

✔ Email Notifications

✔ Dashboard Integration

✔ Historical Analytics

✔ Automated Data Pipeline

---

# 📂 Project Structure

```
atmosync
│
├── src
│
├── python
│     ├── iot_simulator.py
│     ├── kafka_consumer.py
│     ├── email_alert.py
│     ├── refresh_pipeline.py
│     ├── generate_sensor_data.py
│     └── requirements.txt
│
├── Dataset
│
├── Dockerfile
├── docker-compose.yml
├── pom.xml
├── README.md
└── .gitignore
```

---

# 🔌 REST API

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/sensor | Fetch all sensor data |
| GET | /api/sensor/{id} | Fetch sensor by ID |
| POST | /api/sensor | Insert sensor data |
| DELETE | /api/sensor/{id} | Delete sensor |

*(Adjust these endpoints if your project uses different URLs.)*

---

# 🗄 Database

Example sensor table:

| Column | Type |
|---------|------|
| id | BIGINT |
| container_id | VARCHAR |
| temperature | DOUBLE |
| humidity | DOUBLE |
| location | VARCHAR |
| timestamp | TIMESTAMP |

---

# ▶ Running the Project

Clone:

```bash
git clone https://github.com/poojachandurkar1-maker/atmosync.git
```

Start Spring Boot:

```bash
mvn spring-boot:run
```

Run the simulator:

```bash
python python/iot_simulator.py
```

Run the consumer:

```bash
python python/kafka_consumer.py
```

---

# 📊 Dashboard

The Power BI dashboard displays:

- Container Status
- Temperature Trends
- Humidity Trends
- Alert Summary
- High Risk Containers

---

# 📈 Future Enhancements

- Snowflake integration
- dbt transformations
- Machine Learning predictions
- Weather API integration
- Kubernetes deployment
- Cloud deployment (AWS/Azure)

---



**Pooja Chandurkar**

GitHub:
https://github.com/poojachandurkar1-maker

