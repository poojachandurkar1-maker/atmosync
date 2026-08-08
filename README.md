# AtmoSync IoT – Real-Time Micro-Climate Arbitrage Analytics

## Project Overview

AtmoSync IoT is a real-time IoT data engineering and analytics project designed
to monitor micro-climate conditions inside shipping containers carrying
perishable commodities.

The system generates simulated IoT sensor telemetry, streams the data through
Apache Kafka, stores the data in PostgreSQL, performs spoilage and arbitrage
analysis, generates recommendations, sends automated email alerts, and
visualizes the results using Power BI.

## Problem Statement

Traditional supply-chain monitoring often depends on external weather data.
However, conditions inside a shipping container can change significantly and
may directly affect perishable commodities.

AtmoSync monitors:

- Container temperature
- Container humidity
- Container ID
- Commodity
- Container location
- Sensor timestamp
- Commodity price
- Market destination
- Distance
- Travel time
- Estimated hours to spoil
- Arbitrage score
- Risk recommendation

The system identifies containers where environmental conditions and
transportation conditions may create a spoilage or financial risk.

## Architecture

IoT Sensor Simulator
        |
        v
Apache Kafka
        |
        v
Kafka Consumer
        |
        v
PostgreSQL
        |
        v
Spoilage & Arbitrage Analytics
        |
        v
Recommendation Engine
        |
        +----------------------+
        |                      |
        v                      v
Gmail Email Alerts         Power BI Dashboard
        |                      |
        v                      v
Operational Action       Business Analytics


## Technologies

- Python
- Apache Kafka
- PostgreSQL
- SQL
- Power BI
- Gmail SMTP
- Windows Batch
- Git
- GitHub


## Main Components

### IoT Simulator

The IoT simulator generates simulated telemetry for 1,000 unique shipping
containers.

Container IDs range from:

CONT001

to

CONT1000

Each container contains sensor information such as temperature, humidity,
commodity, location, price, and timestamp.

### Commodities

The simulator supports six perishable commodities:

- Avocado
- Apple
- Banana
- Mango
- Tomato
- Strawberry

Each commodity has different temperature requirements and price information.

### Kafka Producer

The Kafka producer publishes IoT telemetry to the Kafka topic:

atmosync-telemetry

Kafka server:

localhost:9092

### Kafka Consumer

The Kafka consumer receives telemetry messages from Kafka and stores the
processed sensor data in PostgreSQL.

Consumer group:

atmosync-consumer

### PostgreSQL

PostgreSQL is used as the central database for storing telemetry and analytical
data.

Database:

atmosyncnew

The database contains sensor data, market information, spoilage calculations,
arbitrage analysis, recommendations, and email alert information.

### Market Destinations

The system evaluates each container against five market destinations.

The market analysis considers:

- Market name
- Distance
- Travel time
- Commodity condition
- Estimated spoilage time
- Arbitrage score

With 1,000 containers and 5 markets:

1,000 Containers × 5 Markets = 5,000 Arbitrage Records


### Spoilage Analytics

The spoilage model estimates the remaining time before a commodity becomes
critical based on environmental conditions.

The analysis uses:

- Commodity
- Temperature
- Humidity
- Storage requirements
- Travel time
- Distance

The main calculated field is:

hours_to_spoil


### Arbitrage Analytics

The arbitrage model evaluates whether a shipment should continue to its
destination or be considered for rerouting.

The analysis produces:

- Distance
- Travel hours
- Hours to spoil
- Temperature
- Humidity
- Arbitrage score

The final analytical dataset contains:

5,000 arbitrage records.


### Recommendation Engine

The recommendation engine converts the arbitrage score into operational
recommendations.

The system uses three categories:

- 🔴 Immediate Reroute
- 🟡 Monitor
- 🟢 Safe

The current recommendation logic is:

Arbitrage Score < 0
        |
        v
🔴 Immediate Reroute

Arbitrage Score 0 to 6
        |
        v
🟡 Monitor

Arbitrage Score > 6
        |
        v
🟢 Safe


### Email Alerts

AtmoSync includes an automated Gmail alert system.

The email alert process checks the recommendation data and identifies
containers with:

🔴 Immediate Reroute

The system generates an email containing:

- Container ID
- Commodity
- Risk status
- Alert message
- Recommended action

The email is sent using Gmail SMTP and a Gmail App Password.

### Email Alert Automation

The email alert process can be executed using the Windows batch file:

python/.bat/run_email_alert.bat

The process writes execution information to:

email_alert.log

Example:

Email alert sent successfully!

At Risk Containers: 160

Alert Process Completed


## Data Volume

The current AtmoSync dataset contains:

- 1,000 unique containers
- 6 commodities
- 5 market destinations
- 5,000 arbitrage records
- 5,000 recommendations
- 160 Immediate Reroute containers

The 5,000 arbitrage records are generated using:

1,000 Containers × 5 Markets = 5,000 Records


## Database Objects

Important PostgreSQL objects include:

- container_telemetry
- market_destinations
- spoilage_model
- spoilage_arbitrage
- arbitrage_recommendation
- email_alerts

The main analytical flow is:

container_telemetry
        |
        v
spoilage_model
        |
        v
spoilage_arbitrage
        |
        v
arbitrage_recommendation
        |
        v
email_alerts


## Power BI Dashboard

Power BI is used as the business intelligence and visualization layer.

The dashboard is designed with two pages.

### Page 1 – Executive Risk & Alert Dashboard

Page 1 provides an executive overview of the current shipment situation.

It includes:

- Total Containers
- Immediate Reroutes
- Monitor Containers
- Safe Containers
- Email Alerts
- Commodity Analysis
- Market Analysis
- Temperature Analysis
- Humidity Analysis
- Arbitrage Score
- Recommendation Status
- Interactive Slicers

The purpose of Page 1 is to quickly identify containers requiring immediate
attention.


### Page 2 – Operational & Detailed Analytics

Page 2 provides detailed analysis for operations and data analysis.

It includes:

- Container-level details
- Commodity analysis
- Market analysis
- Distance analysis
- Travel time
- Hours to spoil
- Temperature
- Humidity
- Arbitrage score
- Recommendation
- Timestamp

The purpose of Page 2 is to allow users to investigate individual containers
and understand the reasons behind the risk.


## Power BI Data Source

Power BI connects to PostgreSQL.

Main analytical source:

public.arbitrage_recommendation

Email alert information is available from:

public.email_alerts

Power BI uses Import mode for the analytical dashboard.


## Business Flow

The complete business process is:

IoT Sensor Data
        |
        v
Real-Time Kafka Streaming
        |
        v
PostgreSQL
        |
        v
Spoilage Analysis
        |
        v
Market Analysis
        |
        v
Arbitrage Score
        |
        v
Risk Recommendation
        |
        +----------------------+
        |                      |
        v                      v
Gmail Alert              Power BI Dashboard
        |                      |
        v                      v
Immediate Action        Business Decision


## Data Validation

The final data is validated using PostgreSQL queries.

### Total Arbitrage Records

Expected:

5,000

### Unique Containers

Expected:

1,000

### Commodities

Expected:

6

### Markets

Expected:

5

### Recommendations

Expected categories:

- 🔴 Immediate Reroute
- 🟡 Monitor
- 🟢 Safe

### Immediate Reroute Containers

Current result:

160


## Project Workflow

The complete project workflow is:

1. Generate IoT sensor data.
2. Publish telemetry to Kafka.
3. Consume Kafka messages.
4. Store telemetry in PostgreSQL.
5. Process commodity and environmental data.
6. Evaluate market destinations.
7. Calculate travel time and spoilage time.
8. Calculate arbitrage scores.
9. Generate recommendations.
10. Store alert information.
11. Send Gmail alerts for critical containers.
12. Refresh Power BI.
13. Analyze business and operational insights.


## Project Structure

AtmoSync-IoT/
|
├── .github/
|
├── config/
│   └── kafka_config.py
|
├── Dataset/
|
├── docs/
|
├── python/
│   ├── email_alert.py
│   ├── generate_sensor_data.py
│   ├── iot_simulator.py
│   ├── kafka_consumer.py
│   ├── refresh_pipeline.py
│   │
│   └── .bat/
│       └── run_email_alert.bat
|
├── sql/
|
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt


## Environment Configuration

Email configuration is stored using environment variables.

Example:

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_APP_PASSWORD=your_gmail_app_password
ALERT_EMAIL=recipient_email@gmail.com

Sensitive credentials should not be committed to GitHub.

The actual `.env` file should remain local.


## Running the Project

### Step 1 – Start PostgreSQL

Start the PostgreSQL database service.

Database:

atmosyncnew


### Step 2 – Start Kafka

Start the Kafka server and make sure Kafka is available at:

localhost:9092


### Step 3 – Start Kafka Consumer

Run:

python -m python.kafka_consumer


### Step 4 – Start IoT Simulator

Run:

python -m python.iot_simulator


### Step 5 – Verify PostgreSQL

Check:

- Total records
- Unique containers
- Commodities
- Market destinations
- Arbitrage records
- Recommendations


### Step 6 – Run Email Alerts

Run:

python -m python.email_alert

or:

python/.bat/run_email_alert.bat


### Step 7 – Refresh Power BI

Refresh the PostgreSQL data in Power BI to display the latest analytics.


## Four-Week Project Development

### Week 1 – IoT Ingestion

- Created project structure
- Developed IoT simulator
- Generated container telemetry
- Configured Apache Kafka
- Created Kafka topic
- Implemented Kafka producer
- Implemented Kafka consumer
- Connected Kafka with PostgreSQL


### Week 2 – Data Processing and Analytics

- Created PostgreSQL database
- Created telemetry tables
- Added commodity information
- Added market destinations
- Developed spoilage calculations
- Developed arbitrage calculations
- Generated 5,000 market analysis records


### Week 3 – Recommendation and Power BI

- Created arbitrage scoring logic
- Created recommendation engine
- Added Immediate Reroute status
- Added Monitor status
- Added Safe status
- Connected PostgreSQL to Power BI
- Created KPI cards
- Created charts
- Added slicers
- Created executive dashboard


### Week 4 – Automation and Final Dashboard

- Created email alert table
- Developed Gmail alert automation
- Configured Gmail SMTP
- Created Windows batch automation
- Implemented automated Immediate Reroute alerts
- Finalized Power BI Page 1
- Developed Power BI Page 2
- Added operational analysis
- Added market analysis
- Added commodity analysis
- Finalized project documentation
- Updated GitHub repository


## Project Goal

The goal of AtmoSync IoT is to create an automated real-time streaming
pipeline capable of detecting environmental and transportation risks in
shipping containers.

The system converts raw IoT sensor data into actionable business insights
through:

- Real-time data streaming
- PostgreSQL analytics
- Spoilage analysis
- Arbitrage scoring
- Risk recommendations
- Automated Gmail alerts
- Power BI dashboards


## Final Project Outcome

AtmoSync demonstrates an end-to-end IoT data engineering and business
intelligence solution:

IoT Simulator
      |
      v
Kafka
      |
      v
PostgreSQL
      |
      v
Analytics
      |
      v
Arbitrage
      |
      v
Recommendations
      |
      +----------------+
      |                |
      v                v
Email Alerts        Power BI
      |                |
      v                v
Operational        Business
Action             Decisions


## Skills Demonstrated

- Python
- SQL
- Apache Kafka
- PostgreSQL
- Data Engineering
- Data Analytics
- Power BI
- DAX
- ETL / ELT concepts
- IoT Data Simulation
- Streaming Data Processing
- Email Automation
- Gmail SMTP
- Windows Batch Automation
- Git
- GitHub
- Business Intelligence


## Future Enhancements

Future versions of AtmoSync can include:

- Real IoT hardware sensors
- GPS tracking
- Real-time cloud deployment
- Machine learning spoilage prediction
- Real market pricing
- Automated route optimization
- Real-time Power BI streaming
- Slack or Teams notifications
- SMS notifications
- Predictive maintenance
- Advanced supply-chain optimization




GitHub:
poojachandurkar1-maker


## Project Summary

AtmoSync transforms real-time IoT telemetry into actionable supply-chain
decisions.

IoT Data
    |
    v
Kafka Streaming
    |
    v
PostgreSQL
    |
    v
Analytics
    |
    v
Arbitrage Score
    |
    v
Risk Recommendation
    |
    +-------------------+
    |                   |
    v                   v
Gmail Alert         Power BI
    |                   |
    v                   v
Immediate Action    Business Insight