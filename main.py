import smtplib
import email_alert as e
import monitor as m
import checksum as c

def main():
    new_csgo_posts = m.get_new_posts()
    if len(new_csgo_posts) > 0:
        new_csgo_strings = '\n'.join(new_csgo_posts)
        f = open('new_csgo_posts.txt', 'w+')
        f.write(new_csgo_strings)
        f.close()

        old_post_hash = c.hashfile('old_csgo_posts.txt')
        new_post_hash = c.hashfile('new_csgo_posts.txt')

        if c.hash_check(old_post_hash, new_post_hash) == True:
            print('No NEW Source 2 posts in /r/GlobalOffensive/new')
            print('Quitting...')
            quit()
        else:
            f = open('old_csgo_posts.txt', 'w+')
            f.write(new_csgo_strings)
            f.close()
            content = new_csgo_strings
            e.email_alert(content)
            print('Success...')
    else:
        print('No Source 2 posts in /r/GlobalOffensive/new')
        quit()

if __name__ == '__main__':
    main()
