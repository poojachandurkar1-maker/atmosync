import os
import psycopg2
import smtplib

from email.mime.text import MIMEText
from dotenv import load_dotenv


# Load .env variables
load_dotenv()


# ==========================================
# PostgreSQL Connection
# ==========================================

conn = psycopg2.connect(
    host="localhost",
    database="atmosyncnew",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()


# ==========================================
# Find Immediate Reroute Containers
# ==========================================

cursor.execute("""
SELECT container_id, commodity
FROM arbitrage_recommendation
WHERE recommendation = '🔴 Immediate Reroute'
""")

rows = cursor.fetchall()


# ==========================================
# Send Email Alert
# ==========================================

if rows:

    message = "AtmoSync Alert - At Risk Containers\n\n"

    for row in rows:
        message += f"Container: {row[0]}\n"
        message += f"Commodity: {row[1]}\n"
        message += "Status: 🔴 Immediate Reroute\n"
        message += "--------------------------------\n"

    # Create email
    msg = MIMEText(message)

    msg["Subject"] = "🔴 AtmoSync - Immediate Reroute Alert"

    # Read email details from .env
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
    ALERT_EMAIL = os.getenv("ALERT_EMAIL")

    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ALERT_EMAIL


    # Connect to Gmail SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    # Login using Gmail App Password
    server.login(
        EMAIL_ADDRESS,
        EMAIL_APP_PASSWORD
    )

    # Send email
    server.send_message(msg)

    # Close connection
    server.quit()

    print("Email alert sent successfully!")
    print("At Risk Containers:", len(rows))


else:

    print("No Immediate Reroute containers found.")


# Close PostgreSQL connection
cursor.close()
conn.close()

print("Alert Process Completed")