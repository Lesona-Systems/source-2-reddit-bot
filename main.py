from pathlib import Path
import email_alert as e
import monitor as m
from checksum import checksum

def main():
    new_csgo_posts = m.get_new_posts()

    f = Path('old_csgo_posts.txt')
    if f.is_file():
        pass
    else:
        f = open(f, 'w')
        f.close()

    if new_csgo_posts:
        new_csgo_strings = '\n'.join(new_csgo_posts)
        write_file('new_csgo_posts.txt', new_csgo_strings)

        if checksum('old_csgo_posts.txt', 'new_csgo_posts.txt'):
            print('No NEW Source 2 posts in /r/GlobalOffensive/new')
            print('Quitting...')
            quit()
        else:
            write_file('old_csgo_posts.txt', new_csgo_strings)
            content = new_csgo_strings
            e.email_alert(content)
            print('Success...')
    else:
        print('No Source 2 posts in /r/GlobalOffensive/new')
        quit()

def write_file(file, content):
    f = open(file, 'w+')
    f.write(content)
    f.close()

if __name__ == '__main__':
    main()
