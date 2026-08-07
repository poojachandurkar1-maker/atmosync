import json
import random
import time
from datetime import datetime, timezone

from kafka import KafkaProducer

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC


TOTAL_RECORDS = 2000

CONTAINERS = [
    "CONT-001",
    "CONT-002",
    "CONT-003",
    "CONT-004",
    "CONT-005",
    "CONT-006",
    "CONT-007",
    "CONT-008",
    "CONT-009",
    "CONT-010",
]

LOCATIONS = [
    "Nagpur",
    "Mumbai",
    "Pune",
    "Delhi",
    "Bengaluru",
    "Hyderabad",
]


def generate_sensor_data():
    """Generate one AtmoSync IoT sensor record."""

    return {
        "container_id": random.choice(CONTAINERS),
        "temperature": round(random.uniform(2.0, 12.0), 2),
        "humidity": round(random.uniform(55.0, 90.0), 2),
        "location": random.choice(LOCATIONS),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def create_kafka_producer():
    """Create Kafka producer."""

    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    )


def main():

    print("=" * 60)
    print("AtmoSync IoT Sensor Simulator")
    print("=" * 60)

    print(f"Kafka Server : {KAFKA_BOOTSTRAP_SERVERS}")
    print(f"Kafka Topic  : {KAFKA_TOPIC}")
    print(f"Total Records: {TOTAL_RECORDS}")
    print("=" * 60)

    producer = create_kafka_producer()

    try:

        for record_number in range(1, TOTAL_RECORDS + 1):

            sensor_data = generate_sensor_data()

            producer.send(
                KAFKA_TOPIC,
                sensor_data
            )

            producer.flush()

            print(
                f"[{record_number}/{TOTAL_RECORDS}] "
                f"{sensor_data}"
            )

            time.sleep(0.1)

        print("=" * 60)
        print(f"Completed successfully: {TOTAL_RECORDS} records sent.")
        print("=" * 60)

    except KeyboardInterrupt:

        print("\nSimulator stopped by user.")

    finally:

        producer.close()


if __name__ == "__main__":
    main()