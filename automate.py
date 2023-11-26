import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def send_email(subject, body, to_email):

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email"  # Replace with your Gmail address
    password = getpass.getpass("Enter your email password: ") #your actual password 

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)

 
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

     
        server.sendmail(sender_email, to_email, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

#