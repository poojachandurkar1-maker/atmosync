CREATE DATABASE atmosync;

CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    container_id VARCHAR(50),
    temperature DECIMAL(5,2),
    humidity DECIMAL(5,2),
    location VARCHAR(100),
    timestamp TIMESTAMP
);