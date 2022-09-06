# source-2-reddit-bot

Monitors new posts in the [Counter-Strike: Global Offensive subreddit](www.reddit.com/r/globaloffensive/new) and returns the any posts with "Source 2" or "source 2" in its title and emails the post title and the post URL to the provided email address.

Pull requests are welcome.

# TODO

- Document cron usage

# Installation

It is strongly recomended to create a virtual environment prior to installation. For further information, please refer to the [Python documentation](https://docs.python.org/3/library/venv.html).

Clone the repository, create & activate your virtual environment, and run:

`pip -r requirements.txt`

## Usage
The [PRAW Python module](https://pypi.org/project/praw/) takes care of the rate limiting to avoid the bot being banned. [secrets.example.ini](secrets.example.ini) contains examples of needed tokens for the bot to run as per directions below.

### Reddit API Secrets
This is a read-only bot. Users will need to create a Reddit application for the PRAW instance to use:

Register a new Reddit application [here](https://www.reddit.com/prefs/apps/).

Create the application as follows:

- Name: [UNIQUE NAME HERE]
- Select "Script"
- Description: [Basic description]
- Redirect URI: 127.0.0.1

Once the bot has been registered, create a `secrets.ini` file in the project root or rename `secrets.example.ini` to `secrets.ini`.

Under `[reddit]` in secrets.ini, enter the following information:

`client_id = [client_id]` - located under `personal use script` on the Reddit bot page.

`client_secret = [client_secret]`

`user_agent = [user_agent]` - manually define `user_agent` using the Reddit application documentation:

Example:
``` <platform>:<app ID>:<version string> (by /u/<reddit username>)```

See [Reddit App/API](https://github.com/reddit-archive/reddit/wiki/API#rules) documentation for more information.

#### Gmail Secrets

##### Gmail Email
There are variables that need to be present under the Gmail header in `secrets.ini`. First is the email address you want the emails to come from. 

In `secrets.ini` ['gmail']['email'], enter the email address from which you want to send the alert.

##### Gmail App Password
Gmail has retired the "Use Less Secure Apps". In order to send emails from a Gmail account with two-factor authentication enabled, users must generate an app password. These application passwords bypass two-factor authentication and cannot be retrieved once they are generated, so be sure to copy it once created.

Follow this [link](https://myaccount.google.com/apppasswords) to name the app and generate your app password. Place generated app password in `secrets.ini` under `email_pass`.
