import tweepy
import json
import os
import sys
import time

usa_location = 23424977


# Emanuele's keys
consumer_key = 	"tVyk6jPU4UPBnaGdHMCGvAY48"
consumer_secret = "QAEViQSW6xE5wRVHwJQP8asDnwXgCmWoN06WE6ep1hgKgIPciQ"

access_token = "841341908957954051-PSaSB6RVihZgvCz0RIlYHr3T4ZGg21E"
access_token_secret = "VMIhfKGvVM9FRMrdq7L1Sy5xWHXid7NF7g7Mc1ZO8JxZi"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

result = api.trends_place(usa_location)
print("["+time.ctime()+"] Start collecting tweets, found "+str(len(result[0]['trends']))+" trending topics")

x=0
y=0
for i in range (0, len(result[0]['trends'])):
    if not os.path.exists("./Tweets/"+result[0]['trends'][i]['name']):
        os.mkdir("./Tweets/"+result[0]['trends'][i]['name'])
    while True:
        try:
            tweets=tweepy.Cursor(api.search, q = result[0]['trends'][i]['name'], show_user = True, tweet_mode='extended').items(100)
            for tw in tweets:
                x+=1
                y+=1
                path="./Tweets/"+result[0]['trends'][i]['name']+"/"+str(tw.user.id)+"";
                f = open(path, 'w')
                if ('retweeted_status' in dir(tw)):
                    f.write(tw.retweeted_status.full_text)
                else:
                    f.write(tw.full_text)
                f.close()
            break
        except tweepy.TweepError:
            print("["+time.ctime()+"] Tweets limit reached, collected "+str(x)+" tweets since last time, "+str(i)+" of "+str(len(result[0]['trends']))+" trending topics examined, retry in 5 minutes...")
            x=0
            time.sleep(300)
            print("["+time.ctime()+"] Retry now...")
            continue;
print("["+time.ctime()+"] End of the process, collected "+str(y)+" tweets!")
