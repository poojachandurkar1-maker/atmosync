import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS",
    "localhost:9092"
)

KAFKA_TOPIC = os.getenv(
    "KAFKA_TOPIC",
    "atmosync-telemetry"
)

KAFKA_GROUP_ID = os.getenv(
    "KAFKA_GROUP_ID",
    "atmosync-consumer"
)

print("AtmoSync Kafka Configuration")
print(f"Kafka Server : {KAFKA_BOOTSTRAP_SERVERS}")
print(f"Kafka Topic  : {KAFKA_TOPIC}")
print(f"Consumer Group: {KAFKA_GROUP_ID}")