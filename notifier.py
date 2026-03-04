import smtplib

EMAIL = "abcd@gmail.com"
PASSWORD = "xxxx xxxx xxxx xxxx"
RECEIVER_EMAIL = "sinchanagowda4758@gmail.com"

def send_alert(api_name):

    subject = f"API Failure Alert: {api_name}"

    body = f"{api_name} API is down. Recovery process triggered."

    message = f"Subject:{subject}\n\n{body}"

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(EMAIL, PASSWORD)

        server.sendmail(EMAIL, EMAIL, message)

        server.quit()

        print("Email alert sent")

    except Exception as e:

        print("Email failed", e)