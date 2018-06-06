import tweepy
import json
import os
import sys
import time

usa_location = 23424977


# Emanuele's keys
consumer_key = 	"MNIY1db3L8UIWbWwcIufdbLsE"
consumer_secret = "EI9DxGIM7BoJOzNHUPjTn3kIPwK8OjNTWgLeWlb46wMg5gvFmE"

access_token = "455678422-G3uLg4O7ulLaZbyVhaSa2zPZamyHjC6eUClw0hUC"
access_token_secret = "gGTh7L7O5P7EhsKiqcESXqA9RXjiafNZOrc5MVXBEap4i"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

'''
# Get all the people the user follows
friends = api.friends_ids()

# Print out each one
for id in friends:
    print(id)
'''

'''
users = []
    page_count = 0
    for user in tweepy.Cursor(api.friends, id=user_id, count=200).pages():
        page_count += 1
        print 'Getting page {} for friends'.format(page_count)
        users.extend(user)
'''
for dir in os.listdir("Tweets"):
    for file in os.listdir("Tweets/" + dir):
        while True:
            try:
                ids_fl = []
                page_count = 0
                for page in tweepy.Cursor(api.followers_ids, id=file, count=5000).pages():
                    page_count += 1
                    ids_fl.extend(page)
                out_fl = open("Tweets/" + dir + "/" + file + " - followers.txt", "w")
                for id in ids_fl:
                    out_fl.write(str(id) + "\n")
                out_fl.close()

                print("-------\n")
                break
            except tweepy.RateLimitError:
                print("["+time.ctime()+"] Tweets limit reached, retry in 15 minutes...")
                time.sleep(910)
                print("["+time.ctime()+"] Retry now...")
                continue;
    print("["+time.ctime()+"] End of the process, collected friends and followers!")
