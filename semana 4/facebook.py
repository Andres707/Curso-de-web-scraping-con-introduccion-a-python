from facebook_scraper import get_posts

for post in get_posts('BinahriaAnalytics', pages=1):
    # print(post['text'][:50])
    print(post)