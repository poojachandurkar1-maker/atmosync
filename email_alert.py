import psycopg2
import smtplib
from email.mime.text import MIMEText

conn = psycopg2.connect(
    host="localhost",
    database="atmosyncnew",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

cursor.execute("""
SELECT container_id, commodity
FROM arbitrage_recommendation
WHERE recommendation='Immediate Reroute'
""")

rows = cursor.fetchall()

if rows:

    message="At Risk Containers\n\n"

    for row in rows:
        message += f"{row[0]} - {row[1]}\n"

    msg=MIMEText(message)

    msg["Subject"]="AtmoSync Alert"

    msg["From"]="poojachandurkar1@gmail.com"

    msg["To"]="poojachandurkar1@gmail.com"

    server=smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login("poojachandurkar1@gmail.com","Pooja123!")

    server.send_message(msg)

    server.quit()

print("Alert Process Completed")