import json
from kafka import KafkaConsumer
import psycopg2

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="atmosyncnew",
    user="postgres",
    password="postgres",   
    port="5432"
)

cursor = conn.cursor()

consumer = KafkaConsumer(
    "container-telemetry",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Listening for Kafka messages...")

for message in consumer:
    data = message.value

    cursor.execute("""
        INSERT INTO container_telemetry
        (container_id, commodity, temperature, humidity, gps_lat, gps_long, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data["container_id"],
        data["commodity"],
        data["temperature"],
        data["humidity"],
        data["gps_lat"],
        data["gps_long"],
        data["timestamp"]
    ))

    conn.commit()

    print("Inserted:", data)