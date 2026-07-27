-- =====================================================
-- AtmoSync - Micro-Climate Arbitrage Analytics
-- Database Script
-- =====================================================

CREATE DATABASE atmosync;

-- Connect to the database
\c atmosync;

-- =====================================================
-- Commodity Table
-- =====================================================

CREATE TABLE commodity (
    commodity_id SERIAL PRIMARY KEY,
    commodity_name VARCHAR(50),
    price_per_kg NUMERIC(10,2),
    max_temperature NUMERIC(5,2),
    max_humidity NUMERIC(5,2)
);

-- Commodity Data
INSERT INTO commodity
(commodity_name, price_per_kg, max_temperature, max_humidity)
VALUES
('Avocado',120.00,25.00,70.00),
('Banana',40.00,26.00,75.00),
('Mango',150.00,30.00,80.00),
('Orange',80.00,27.00,70.00),
('Tomato',60.00,28.00,75.00);

---Create Health View
CREATE VIEW vw_container_health AS

SELECT

    s.container_id,

    c.commodity_name,

    c.price_per_kg,

    c.max_temperature,

    c.max_humidity,

    s.temperature,

    s.humidity,

    s.location,

    s.timestamp,

    CASE

        WHEN s.temperature > c.max_temperature

        OR s.humidity > c.max_humidity

        THEN 'At Risk'

        ELSE 'Healthy'

    END AS health_status

FROM sensor_data s

JOIN container_mapping cm

ON s.container_id = cm.container_id

JOIN commodity c

ON cm.commodity_id = c.commodity_id;

---Create Spoilage Analytics View
CREATE VIEW vw_spoilage_analytics AS

SELECT

    *,

    CASE

        WHEN health_status='At Risk'

        THEN 70

        ELSE 10

    END AS spoilage_percent,

    (price_per_kg *

        CASE

            WHEN health_status='At Risk'

            THEN 70

            ELSE 10

        END

    )/100 AS "Revenue At Risk"

FROM vw_container_health;

---Analysis Queries
1.Total Records
SELECT COUNT(*) FROM sensor_data;

2.Average Temperature
SELECT ROUND(AVG(temperature)::numeric,2)
FROM sensor_data;

3.Average Humidity
SELECT ROUND(AVG(humidity)::numeric,2)
FROM sensor_data;

4.Commodity-wise Average Temperature
SELECT
commodity_name,
ROUND(AVG(temperature)::numeric,2)
FROM vw_container_health
GROUP BY commodity_name;

5.Revenue At Risk
SELECT
SUM("Revenue At Risk")
FROM vw_spoilage_analytics;

6.Health Status Count
SELECT
health_status,
COUNT(*)
FROM vw_spoilage_analytics
GROUP BY health_status;

7.Location-wise Containers
SELECT
location,
COUNT(DISTINCT container_id)
FROM vw_spoilage_analytics
GROUP BY location;

