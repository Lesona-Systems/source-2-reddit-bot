import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import parse_config as p

def email_alert(mail_content): 
    # parse secrets.ini for required credentials
    sender_address = p.get_user_email()
    sender_pass = p.get_gmail_app_pass()
    recipient_address = p.get_user_email()

    # construct message object
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = recipient_address
    message['Subject'] = 'New Source 2 Post in /r/globaloffensive'

    # create body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session to send the email
    session = smtplib.SMTP('smtp.gmail.com', 587)

    # upgrade session to SSL & login
    session.starttls()
    session.login(sender_address, sender_pass)

    # format message as string, pass to session & send email
    text = message.as_string()
    session.sendmail(sender_address, recipient_address, text)
    session.quit()
