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
                ids_fr = []
                page_count = 0
                for page in tweepy.Cursor(api.friends_ids, id=file, count=5000).pages():
                    page_count += 1
                    ids_fr.extend(page)
                out_fr = open("Tweets/" + dir + "/" + file + " - friends.txt", "w")
                for id in ids_fr:
                    out_fr.write(str(id) + "\n")
                out_fr.close()

                print("~~~~~~~\n")
                break
            except tweepy.RateLimitError:
                print("["+time.ctime()+"] Tweets limit reached, retry in 15 minutes...")
                time.sleep(910)
                print("["+time.ctime()+"] Retry now...")
                continue;
    print("["+time.ctime()+"] End of the process, collected friends and followers!")
