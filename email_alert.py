import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import parse_config as p

def email_alert(mail_content): 
    #The mail addresses and password
    sender_address = p.get_user_email()
    sender_pass = p.get_gmail_app_pass()
    receiver_address = 'nejwritings@gmail.com'

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'New Source 2 Post in /r/globaloffensive'   #The subject line

    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)

    session.starttls() #enable security
    session.login(sender_address, sender_pass)

    #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
