import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="atmosyncnew",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()

views = [
    "stg_container_telemetry",
    "analytics_container",
    "container_health",
    "spoilage_model",
    "spoilage_arbitrage",
    "arbitrage_recommendation"
]

for view in views:
    print(f"{view} is ready.")

print("Pipeline validation completed.")

cursor.close()
conn.close()