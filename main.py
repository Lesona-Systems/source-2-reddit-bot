import smtplib
import email_alert as e
import monitor as m
import checksum as check

def main():
    s2_post_exists = m.monitor()
    # hacky item separation
    post_information = ' : '.join([s2_post_exists[1], s2_post_exists[2]])

    if s2_post_exists[0] == True:
        e.email_alert(post_information)
        print('Success...')
    else:
        quit

main()
