import pandas as pd
from faker import Faker
import random
from sqlalchemy import create_engine

fake = Faker()

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/atmosync"
)

records = []

for i in range(10000):
    records.append({
        "container_id": f"CONT{random.randint(100,999)}",
        "temperature": round(random.uniform(15,40),2),
        "humidity": round(random.uniform(40,95),2),
        "location": fake.city(),
        "timestamp": fake.date_time_this_year()
    })

df = pd.DataFrame(records)

df.to_sql(
    "sensor_data",
    engine,
    if_exists="append",
    index=False
)

print("10000 sensor records inserted successfully!")