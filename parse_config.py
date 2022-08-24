from configparser import ConfigParser
config = ConfigParser()

def get_client_secret():
    config.read('secrets.ini')
    return config['reddit']['client_secret']

def get_client_id():
    config.read('secrets.ini')
    return config['reddit']['client_id']

def get_user_agent():
    config.read('secrets.ini')
    return config['reddit']['user_agent']

def get_user_email():
    config.read('secrets.ini')
    return config['gmail']['email']

def get_gmail_app_pass():
    config.read('secrets.ini')
    return config['gmail']['email_pass']

def get_receiver_address():
    config.read('secrets.ini')
    return config['email']['address']
