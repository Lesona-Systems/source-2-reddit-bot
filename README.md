# source-2-reddit-bot
Monitors reddit.com/r/globaloffensive and returns the first instance of a post with "Source 2" or "source 2" in its title and emails the post title and its URL to the given email address.

Currently running on a RaspberryPi B+. 

Pull requests are welcome.

**TO DO**

** Document cron usage **
** Do not send email if returned post titles are unchanged despite fulfilling if statements **
** Return multiple post titles **

## Usage

Personal project for gaining experience in scraping Reddit (using PRAW) to look for mentions of "Source 2" in /r/GlobalOffensive's "New" catagory. Unfinished.

### Installation

It is strongly recomended to create a virtual environment prior to installation. For further information, please refer to the [Python documentation](https://docs.python.org/3/library/venv.html).

Download latest release and run 

`python -r requirements.txt` on Windows

`python3 -r requirements.txt` on MacOS & Linux.

### Usage
The PRAW module does a fantastic job of taking care of the rate limiting to avoid your bot being banned. [secrets.example.ini](secrets.example.ini) will contain all the needed tokens for the bot to run, but it does require some setup on your end.

#### Reddit API Secrets
This is a read-only bot, meaning that we'll need fewer tokens than if the bot was reading/replying to comments. Regardless, users will need to create a Reddit application for the PRAW instance to use:

Register a new Reddit application [here](https://www.reddit.com/prefs/apps/).

Create the application as follows:

- Name: [UNIQUE NAME HERE]
- Select "Script"
- Description: [Basic description]
- Redirect URI: 127.0.0.1

Once the bot has been registered, create a `secrets.ini` file in the project root or rename `secrets.example.ini` to `secrets.ini`.

Under `[reddit]` in secrets.ini, enter the following information:

`client_id = [client_id]` - located under `personal use script`


`client_secret = [client_secret]`


`user_agent = [user_agent]` - manually define `user_agent` using the Reddit application documentation:

Example:
``` <platform>:<app ID>:<version string> (by /u/<reddit username>)```

See [Reddit App](https://github.com/reddit-archive/reddit/wiki/API#rules) documentation for more information.

#### Gmail Secrets

##### Gmail Email
There are two fields that need to be filled out for the Gmail dictionary in `secrets.ini`. First is the email address you want the emails to come from. 

In `secrets.ini` ['gmail']['email'], enter the email address from which you want to send the alert.

##### Gmail App Password
Gmail has retired the "Use Less Secure Apps", meaning that in order to send emails from a Gmail account with two-factor authentication enabled, users must generate an app password.

These application passwords bypass two-factor authentication and cannot be retrieved once they are generated, so be sure to copy it once genereated.

Follow this [link](https://myaccount.google.com/apppasswords) to name the app and generate your app password. Place generated app password in `secrets.ini` under `email_pass`.

