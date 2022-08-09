import smtplib
import email_alert as email
import monitor as m

def main():
    s2_post_exists = m.monitor()

    post_information = '    '.join([s2_post_exists[1], s2_post_exists[2]])

    if s2_post_exists[0] == True:
        email.email_alert(post_information)
    else:
        quit

main()