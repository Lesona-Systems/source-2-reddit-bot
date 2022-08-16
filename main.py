import smtplib
import email_alert as e
import monitor as m
import checksum as c

def main():
    new_csgo_posts = m.get_new_posts()
    new_csgo_strings = '\/n'.join(new_csgo_posts)
    f = open('new_csgo_posts.txt', 'w+')
    f.write(new_csgo_strings)
    f.close()

    old_post_hash = c.hashfile('old_csgo_posts.txt')
    new_post_hash = c.hashfile('new_csgo_posts.txt')

    if c.hash_check(old_post_hash, new_post_hash) == True:
        print('No new Source 2 posts on /r/GlobalOffensive')
        print('Quitting...')
        quit()
    else:
        f = open('old_csgo_posts.txt', 'w+')
        f.write(new_csgo_strings)
        f.close()
        content = new_csgo_strings
        e.email_alert(content)
        print('Success...')

if __name__ == '__main__':
    main()
