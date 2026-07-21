import pandas as pd
import random
from faker import Faker
from sqlalchemy import create_engine
from datetime import datetime, timedelta

fake = Faker()

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/atmosync"
)

records = []

locations = [
    "Nagpur",
    "Mumbai",
    "Delhi",
    "Pune",
    "Hyderabad",
    "Bangalore"
]

for i in range(10000):

    records.append({

        "container_id": f"CONT{random.randint(1000,9999)}",

        "temperature": round(random.uniform(5,45),2),

        "humidity": round(random.uniform(20,95),2),

        "location": random.choice(locations),

        "timestamp":
        datetime.now()-timedelta(hours=random.randint(0,720))

    })

df = pd.DataFrame(records)

df.to_sql(
    "sensor_data",
    engine,
    if_exists="append",
    index=False
)

print("10000 Records Inserted Successfully")
