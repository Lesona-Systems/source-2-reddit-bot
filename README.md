# source-2-reddit-bot
Monitors reddit.com/r/globaloffensive and returns the first instance of a post with "Source 2" or "source 2" in its title and emails the post title and its URL to the given email address. Currently running on a RaspberryPi B+. 

Pull requests are welcome.

## Usage

Personal project for gaining experience in scraping Reddit (using PRAW) to look for mentions of "Source 2" in /r/GlobalOffensive 's "New" catagory. Unfinished.

### Installation

It is strongly recomended to create a virtual environment prior to installation. For further information, please refer to the [Python documentation](https://docs.python.org/3/library/venv.html).

Download latest release and run 

```python -r requirements.txt```

on Windows or

```python3 -r requirements.txt```

on MacOS & Linux.

### Usage

The PRAW module does a fantastic job of taking care of the rate limiting to avoid your bot being banned. [secrets.example.ini](secrets.example.ini) will contain all the needed tokens for the bot to run, but it does require some setup on your end.


#### Reddit API Secrets

This is a read-only bot, meaning that we'll need fewer tokens than if the bot was reading/replying to comments. Regardless, users will need to create a Reddit bot on [Reddit.com]()

In order to use the bot, users must register an application [here](https://www.reddit.com/prefs/apps/). Create the application as shown, with the RedirectURI as your localhost: 127.0.0.1:

![Reddit Bot](https://imgur.com/AhEnsGi)

You'll then take the information from this page and fill it in to your own secrets.ini.

```[reddit]
client_id = [client_id]
client_secret = [client_secret]
user_agent = [user_agent]```

The ```client_id``` is 
