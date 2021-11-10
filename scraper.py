from facebook_scraper import get_posts

#name of facebook page
name = 'partia.korwin.jkm'

people = {}

for post in get_posts(name, pages = 1, options = {"comments": True}, cookies = 'cookies.txt'):
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
