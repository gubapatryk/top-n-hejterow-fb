###################################################################
#               Extracting the data from website                  #
###################################################################

from facebook_scraper import get_posts

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def scrape(name = 'cnn', _pages = 1):
    #name of facebook page

    result = ""

    people = {}

    for post in get_posts(name, pages = _pages, options = {"comments": True}, cookies = 'cookies.txt'):#cridentials = ('mvboevfegkjaktnqlq@sdvrecft.com', 'jadro123'),
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
                re_text = reply['comment_text']#.encode()
                if re_text != 'None':
                    if re_name in people:
                        people[re_name].append(re_text)
                    else:
                        people[re_name] = [re_text]
    overall = 0
    for person, comments in people.items():
        overall += len(comments)
        result += '\n' + person + ' made ' + str(len(comments)) + ' comments'
    result += '\n' + ('overall there are {} comments to be analyzed'.format(overall))

    ###################################################################
    #       Analyzing the comments using Azure Cognitive Services     #
    ###################################################################

    key = ""
    endpoint = "https://comment-analyzer.cognitiveservices.azure.com/"


    # Authenticate the client using your key and endpoint
    def authenticate_client():
        ta_credential = AzureKeyCredential(key)
        text_analytics_client = TextAnalyticsClient(
                endpoint = endpoint,
                credential = ta_credential)
        return text_analytics_client

    client = authenticate_client()

    # function for detecting negative sentiment in comments
    def is_negative(comment, client):
        response = client.analyze_sentiment(documents = [comment])[0]
        return (response.sentiment == "negative")

    negative_comments = []
    count = 0
    for person, comments in people.items():
        tmp = [0, person, []]
        for comment in comments:
            if is_negative(comment, client):
                tmp[0] += 1
                tmp[2].append(comment)
        if tmp[0] > 0:
            negative_comments.append(tmp)
            count += tmp[0]

    result += "\noverall there are " + str(count) + " negative comments"

    negative_comments.sort(reverse = True)

    for hater in range(min(5, len(negative_comments))):
        result += '\n' + negative_comments[hater][1] + " made " + str(negative_comments[hater][0]) + " negative comments, first 5: " + str(negative_comments[hater][2][:5])
    return result
