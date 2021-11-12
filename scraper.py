# CNN's profile might already be moderated


from facebook_scraper import get_posts
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

#name of facebook page
name = 'cnn'

people = {}

for post in get_posts(name, pages = 10, options = {"comments": True}, cookies = 'cookies.txt'):
    for comment in post['comments_full']:
        #original commenter name
        op_name = comment['commenter_name']
        op_text = comment['comment_text']
        if op_text != 'None':
            if op_name in people:
                people[op_name].append(op_text)
            else:
                people[op_name] = [op_text]
        for reply in comment['replies']:
            #replier name
            re_name = reply['commenter_name']
            re_text = reply['comment_text']
            if re_text != 'None':
                if re_name in people:
                    people[re_name].append(re_text)
                else:
                    people[re_name] = [re_text]

for person, comments in people.items():
    print(person, 'made', str(len(comments)), 'comments')

sia = SentimentIntensityAnalyzer()

negative_comments = []

for person, comments in people.items():
    tmp = [0, person, []]
    for comment in comments:
        if sia.polarity_scores(comment)["compound"] < 0:
            tmp[0] += 1
            tmp[2].append(comment)
    if tmp[0] > 0:
        negative_comments.append(tmp)

negative_comments.sort()

for hater in range(5):
    print(negative_comments[hater][1], "made", negative_comments[hater][0], "negative_comments, first 5:", negative_comments[hater][2][:5])
