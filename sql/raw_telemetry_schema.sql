-- ==========================================
-- AtmoSync Raw Telemetry Table
-- ==========================================

CREATE DATABASE atmosync;

-- Connect to database
-- PostgreSQL:
-- \c atmosync;


CREATE TABLE IF NOT EXISTS raw_telemetry (
    id SERIAL PRIMARY KEY,
    container_id VARCHAR(50),
    temperature DECIMAL(5,2),
    humidity DECIMAL(5,2),
    location VARCHAR(50),
    event_timestamp TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);