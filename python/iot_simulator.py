import json
import random
import time
from datetime import datetime, timezone

from kafka import KafkaProducer

import sys
import os


# ============================================================
# Allow importing config from project root
# ============================================================

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from config.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC
)


# ============================================================
# AtmoSync IoT Sensor Simulator Configuration
# ============================================================

# Exactly 1,000 records
TOTAL_RECORDS = 1000

# Exactly 1,000 unique containers
# CONT001 ... CONT999 ... CONT1000
CONTAINERS = [
    f"CONT{i:03d}"
    for i in range(1, 1001)
]


# ============================================================
# Commodity Configuration
# ============================================================

COMMODITIES = {
    "Avocado": {
        "price": 180,
        "min_temp": 2,
        "max_temp": 7
    },

    "Apple": {
        "price": 140,
        "min_temp": 1,
        "max_temp": 6
    },

    "Banana": {
        "price": 90,
        "min_temp": 12,
        "max_temp": 14
    },

    "Mango": {
        "price": 120,
        "min_temp": 8,
        "max_temp": 13
    },

    "Tomato": {
        "price": 70,
        "min_temp": 8,
        "max_temp": 12
    },

    "Strawberry": {
        "price": 350,
        "min_temp": 0,
        "max_temp": 4
    }
}


# ============================================================
# Locations
# ============================================================

LOCATIONS = [
    "Nagpur",
    "Mumbai",
    "Pune",
    "Delhi",
    "Bengaluru",
    "Hyderabad"
]


# ============================================================
# Generate IoT Sensor Data
# ============================================================

def generate_sensor_data(container_id, commodity):
    """
    Generate one AtmoSync IoT sensor record
    for a specific container and commodity.
    """

    commodity_info = COMMODITIES[commodity]

    # Generate temperature around the commodity's
    # recommended storage range.
    temperature = round(
        random.uniform(
            commodity_info["min_temp"] - 3,
            commodity_info["max_temp"] + 3
        ),
        2
    )

    humidity = round(
        random.uniform(55.0, 90.0),
        2
    )

    return {
        "container_id": container_id,
        "commodity": commodity,
        "temperature": temperature,
        "humidity": humidity,
        "price_per_kg": commodity_info["price"],
        "location": random.choice(LOCATIONS),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


# ============================================================
# Create Kafka Producer
# ============================================================

def create_kafka_producer():
    """Create Kafka producer."""

    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda value: json.dumps(value).encode("utf-8")
    )


# ============================================================
# Main Simulator
# ============================================================

def main():

    print("=" * 70)
    print("AtmoSync IoT Sensor Simulator")
    print("=" * 70)

    print(f"Kafka Server     : {KAFKA_BOOTSTRAP_SERVERS}")
    print(f"Kafka Topic      : {KAFKA_TOPIC}")
    print(f"Total Records    : {TOTAL_RECORDS}")
    print(f"Total Containers : {len(CONTAINERS)}")
    print(f"Total Commodities: {len(COMMODITIES)}")

    print("=" * 70)

    print("Commodities:")
    
    for commodity, details in COMMODITIES.items():
        print(
            f"  {commodity:<12} "
            f"Price: ₹{details['price']}/kg | "
            f"Temperature: {details['min_temp']}°C - "
            f"{details['max_temp']}°C"
        )

    print("=" * 70)

    # Create Kafka producer
    producer = create_kafka_producer()

    # Convert commodity dictionary to list
    commodity_list = list(COMMODITIES.keys())

    try:

        # ====================================================
        # One record for each container
        # ====================================================

        for record_number, container_id in enumerate(
            CONTAINERS,
            start=1
        ):

            # Distribute commodities evenly.
            #
            # CONT001 -> Avocado
            # CONT002 -> Apple
            # CONT003 -> Banana
            # CONT004 -> Mango
            # CONT005 -> Tomato
            # CONT006 -> Strawberry
            # CONT007 -> Avocado
            # ...
            #
            commodity = commodity_list[
                (record_number - 1) % len(commodity_list)
            ]

            # Generate sensor record
            sensor_data = generate_sensor_data(
                container_id,
                commodity
            )

            # Send record to Kafka
            producer.send(
                KAFKA_TOPIC,
                sensor_data
            )

            # Make sure message is delivered
            producer.flush()

            # Display record
            print(
                f"[{record_number}/{TOTAL_RECORDS}] "
                f"{sensor_data}"
            )

            # Small delay between messages
            time.sleep(0.1)

        print("=" * 70)
        print("Simulation Completed Successfully!")
        print(f"Records Sent     : {TOTAL_RECORDS}")
        print(f"Containers Used  : {len(CONTAINERS)}")
        print(f"Commodities Used : {len(COMMODITIES)}")
        print("=" * 70)

    except KeyboardInterrupt:

        print("\nSimulator stopped by user.")

    finally:

        producer.close()


# ============================================================
# Run Application
# ============================================================

if __name__ == "__main__":
    main()