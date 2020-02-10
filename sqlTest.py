import pypyodbc 
import praw
import pandas

redditConnect = praw.Reddit(client_id='PF6tIWliuJ_oQw', \
                     client_secret='sNg8bh-UZVV9QVLb9oqX2nFBEiQ', \
                     user_agent='firstTest', \
                     username='uncomfortablyhigh', \
                     password='fred43')


subreddit = redditConnect.subreddit('LonghornNation')

hot_subreddit = subreddit.new(limit=1000)

connection = pypyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost;'
    r'DATABASE=redditAPI;'
    r'Trusted_Connection=yes;'
)
cursor = connection.cursor()

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()


 

 
for submission in subreddit.top(limit=1):
    print(submission.title)

    #testing changes