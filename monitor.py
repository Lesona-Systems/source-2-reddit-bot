import parse_config as p
import praw

def monitor():

    reddit = praw.Reddit(
        client_id = p.get_client_id(),
        client_secret = p.get_client_secret(),
        user_agent = p.get_user_agent(),
    )

    for post in reddit.subreddit('globaloffensive').new():
        if "Source 2" in post.title or "source 2" in post.title:
            url = "https://www.reddit.com" + post.permalink
            return(True, post.title, url)
        else:
            pass