import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "YOUR EMAIL NEED TO GIVE "  # Replace with your email
SENDER_PASSWORD = "EMAIL APP PASSWORD"  # Replace with your app-specific password

# Load email recipients from CSV
def load_recipients(csv_file):
    recipients = []
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            recipients.append(row)
    return recipients

# Email template
def get_email_content(name):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <title>GDG on Campus Workshop Invitation</title>
        YOUR HTML EMAIL TEMPLATE"""
        

# Send email function
def send_email(to_email, name):
    try:
        # Prepare the email content
        msg = MIMEMultipart("alternative")
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = "your Subject email"

        # Add HTML content
        html_content = get_email_content(name)
        msg.attach(MIMEText(html_content, "html"))

        # Connect to the server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
            print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Main script
if __name__ == "__main__":
    # Path to the CSV file containing recipients
    csv_file = "Your csv file"  # Ensure the file has 'Name' and 'Email' columns

    # Load recipients from the CSV file
    recipients = load_recipients(csv_file)

    # Send emails to all recipients
    for recipient in recipients:
        send_email(recipient["Email"], recipient["Name"])
