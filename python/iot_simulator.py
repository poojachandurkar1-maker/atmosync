import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

containers = ["CONT001", "CONT002", "CONT003", "CONT004", "CONT005"]
commodities = ["Avocado", "Banana", "Apple", "Tomato", "Mango"]

print("AtmoSync IoT Simulator Started...")

while True:

    telemetry = {
        "container_id": random.choice(containers),
        "commodity": random.choice(commodities),
        "temperature": round(random.uniform(2, 15), 2),
        "humidity": random.randint(60, 95),
        "gps_lat": round(random.uniform(18.5200, 18.6200), 6),
        "gps_long": round(random.uniform(73.8200, 73.9200), 6),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send("container-telemetry", telemetry)
    producer.flush()

    print("Sent:", telemetry)

    time.sleep(2)