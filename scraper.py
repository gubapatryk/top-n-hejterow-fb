from facebook_scraper import get_posts

#name of facebook page
name = 'partia.korwin.jkm'

for post in get_posts(name, pages = 1, options = {"comments": True}, cookies = 'cookies.txt'):
    print(post)
