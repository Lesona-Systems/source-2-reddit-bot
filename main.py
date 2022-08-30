from pathlib import Path
import email_alert as e
import monitor as m
from checksum import checksum

def main():
    # get new posts from Reddit
    new_csgo_posts = m.get_new_posts()

    # check for old_csgo_posts.txt. If it doesn't exist, create it and move on.
    f = Path('old_csgo_posts.txt')
    if f.is_file():
        pass
    else:
        f = open(f, 'w')
        f.close()

    # if there are any posts that meet the criteria on Reddit, grab them and write them to new_csgo_posts.txt
    if new_csgo_posts:
        new_csgo_strings = '<br>'.join(new_csgo_posts)
        write_file('new_csgo_posts.txt', new_csgo_strings)

    # hash and compare old_csgo_posts.txt and new_csgo_posts.txt.
    # if hashes match, quit.
        if checksum('old_csgo_posts.txt', 'new_csgo_posts.txt'):
            print('No NEW Source 2 posts in /r/GlobalOffensive/new \n Quitting....')
            quit()
    # if hashes DO NOT match, email the alert and write posts to file for next run hash comparison
        else:
            write_file('old_csgo_posts.txt', new_csgo_strings)
            e.email_alert(new_csgo_strings)
            print('Success...')
    # if criteria isn't met, tell user and quit
    else:
        print('No Source 2 posts in /r/GlobalOffensive/new \n Quitting....')
        quit()

def write_file(file, content):
    f = open(file, 'w+')
    f.write(content)
    f.close()

if __name__ == '__main__':
    main()
