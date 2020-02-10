import praw
import pandas
 
redditConnect = praw.Reddit(client_id='PF6tIWliuJ_oQw', \
                     client_secret='sNg8bh-UZVV9QVLb9oqX2nFBEiQ', \
                     user_agent='firstTest', \
                     username='uncomfortablyhigh', \
                     password='fred43')


subreddit = redditConnect.subreddit('LonghornNation')

hot_subreddit = subreddit.new(limit=1000)
 
for submission in subreddit.top(limit=1):
    print(submission.title)