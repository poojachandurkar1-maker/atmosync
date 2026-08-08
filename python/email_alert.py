```python
import os
import psycopg2
import smtplib

from email.mime.text import MIMEText
from dotenv import load_dotenv


# ============================================================
# Load .env variables
# ============================================================

load_dotenv()


# ============================================================
# PostgreSQL Connection
# ============================================================

conn = psycopg2.connect(
    host="localhost",
    database="atmosyncnew",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()


try:

    # ========================================================
    # Find Immediate Reroute Containers
    # ========================================================

    cursor.execute("""
        SELECT container_id, commodity
        FROM arbitrage_recommendation
        WHERE recommendation = '🔴 Immediate Reroute'
    """)

    rows = cursor.fetchall()


    # ========================================================
    # Send Email Alert
    # ========================================================

    if rows:

        message = "AtmoSync Alert - At Risk Containers\n\n"

        for row in rows:
            message += f"Container: {row[0]}\n"
            message += f"Commodity: {row[1]}\n"
            message += "Status: 🔴 Immediate Reroute\n"
            message += "--------------------------------\n"


        # ====================================================
        # Create Email
        # ====================================================

        msg = MIMEText(message)

        msg["Subject"] = "🔴 AtmoSync - Immediate Reroute Alert"


        # ====================================================
        # Read Email Details from .env
        # ====================================================

        EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
        ALERT_EMAIL = os.getenv("ALERT_EMAIL")

        msg["From"] = EMAIL_ADDRESS
        msg["To"] = ALERT_EMAIL


        # ====================================================
        # Connect to Gmail SMTP
        # ====================================================

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(
            EMAIL_ADDRESS,
            EMAIL_APP_PASSWORD
        )


        # ====================================================
        # Send Email
        # ====================================================

        server.send_message(msg)

        server.quit()


        print("Email alert sent successfully!")
        print("At Risk Containers:", len(rows))


        # ====================================================
        # UPDATE EMAIL ALERT STATUS
        # ====================================================
        #
        # Gmail has successfully sent the alert.
        # Now update the corresponding records in PostgreSQL:
        #
        # Pending → Sent
        #
        # ====================================================

        container_ids = [row[0] for row in rows]

        cursor.execute("""
            UPDATE email_alerts
            SET status = 'Sent'
            WHERE container_id = ANY(%s)
              AND status = 'Pending'
        """, (container_ids,))


        # ====================================================
        # Save Database Changes
        # ====================================================

        conn.commit()

        print(
            "Email alert database status updated successfully!"
        )

        print(
            "Alerts marked as Sent:",
            cursor.rowcount
        )


    else:

        print("No Immediate Reroute containers found.")


except Exception as e:

    # ========================================================
    # Error Handling
    # ========================================================

    conn.rollback()

    print("ERROR:", str(e))

    print(
        "Email alert process failed. "
        "Database changes were rolled back."
    )


finally:

    # ========================================================
    # Close PostgreSQL Connection
    # ========================================================

    cursor.close()
    conn.close()

    print("Alert Process Completed")
```
