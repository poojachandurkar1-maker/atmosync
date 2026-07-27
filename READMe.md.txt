# 🚛 AtmoSync – Micro-Climate Arbitrage Analytics

## 📌 Project Overview

AtmoSync is an end-to-end data analytics project that monitors agricultural commodity shipments using IoT sensor data. The system analyzes temperature, humidity, and container health to identify spoilage risks and estimate financial losses before commodities reach the destination.

This project demonstrates PostgreSQL database design, SQL analytics, and interactive Power BI dashboard development.

---

# 🎯 Problem Statement

Traditional supply chain analytics rely on macro weather forecasts and estimated transit times. They cannot detect real-time micro-climate changes occurring inside shipping containers.

A sudden increase in temperature or humidity can reduce commodity quality and increase financial losses.

AtmoSync provides a real-time monitoring solution that identifies at-risk containers and supports proactive logistics decisions.

---

# 🚀 Objectives

- Monitor container temperature and humidity
- Calculate spoilage risk
- Detect unhealthy containers
- Estimate revenue at risk
- Visualize container performance
- Support business decision-making

---

# 🛠 Technology Stack

- PostgreSQL
- SQL
- Power BI
- CSV
- GitHub

---

# 📂 Database Tables

## commodity

Stores commodity information.

| Column |
|---------|
| commodity_id |
| commodity_name |
| price_per_kg |
| max_temperature |
| max_humidity |

---

## sensor_data

Stores IoT sensor readings.

| Column |
|---------|
| id |
| container_id |
| temperature |
| humidity |
| location |
| timestamp |

---

## container_mapping

Maps containers to commodities.

| Column |
|---------|
| container_id |
| commodity_id |

---

# 📊 Dashboard Pages

## Executive Dashboard

- KPI Cards
- Average Temperature
- Average Humidity
- Revenue at Risk
- Spoilage Rate
- Commodity Analysis
- Location Analysis
- Scatter Plot
- Temperature Trend
- Interactive Filters

---

## Container Monitoring

- Container Filter
- Health Status
- Temperature
- Humidity
- Spoilage Percentage
- Trend Analysis
- Detail Table

---

# 📈 KPIs

- Total Containers
- Average Temperature
- Average Humidity
- Average Spoilage
- Revenue at Risk
- Healthy Containers
- At Risk Containers

---

# 📊 SQL Views

vw_container_health

Calculates health status of each shipment.

---

vw_spoilage_analytics

Calculates spoilage percentage and revenue at risk.

---

# 💼 Business Insights

- Identify high-risk containers.
- Monitor environmental conditions.
- Reduce spoilage losses.
- Improve logistics planning.
- Increase supply chain efficiency.

---

# 📷 Dashboard Preview

Executive Dashboard

Container Monitoring Dashboard

(Add screenshots here)

---

# 📁 Folder Structure

```
AtmoSync
│
├── Dataset
├── SQL
├── PowerBI
├── Documentation
├── Images
└── Presentation
