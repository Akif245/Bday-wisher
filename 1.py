import smtplib
import datetime
from email.message import EmailMessage
import ssl

# Birthday list with email
birthdays = {
    "Mohit": {"date": "2005-05-08", "email": "mohit@example.com"},
    "Akif": {"date": "2005-05-08", "email": "abdulakif44570@gmail.com"},
}

# Email credentials (Use App Password for Gmail)
EMAIL_SENDER = "245123733173@mvsrec.edu.in"
EMAIL_PASSWORD ="sdgsfdg"

# Get today's date
today = datetime.date.today()

# Loop through birthdays
for name, details in birthdays.items():
    bday = datetime.datetime.strptime(details["date"], "%Y-%m-%d").date()
    if bday.day == today.day and bday.month == today.month:
        # Prepare email
        msg = EmailMessage()
        msg["Subject"] = f"Happy Birthday, {name}! 🎉"
        msg["From"] = EMAIL_SENDER
        msg["To"] = details["email"]
        msg.set_content(f"Dear {name},\n\n🎂 Happy Birthday! Wishing you a fantastic year ahead.\n\nBest wishes,\nAkif")

        # Send the email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"✅ Birthday email sent to {name} at {details['email']}")
