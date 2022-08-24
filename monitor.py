import parse_config as p
import praw

post_entries = []

def get_new_posts():

    # init reddit class w/ PRAW
    reddit = praw.Reddit(
        client_id = p.get_client_id(),
        client_secret = p.get_client_secret(),
        user_agent = p.get_user_agent(),
    )

    for post in reddit.subreddit('globaloffensive').new():
        if "Source 2" in post.title or "source 2" in post.title:
            url = "https://www.reddit.com" + post.permalink
            post_entry = [post.title, url]
            post_entry = '  '.join(post_entry)
            post_entries.append(post_entry)
        else:
            pass

    return post_entries
    