import os

tweets="Tweets"
tweets_folders=os.listdir(tweets)
n_tweets=0
n_followers=0
n_friends=0

for dir in tweets_folders:
    if (".txt" in dir):
        continue
    if (".DS_Store" in dir):
        continue
    dir_files=os.listdir(os.path.join(tweets, dir))

    for file in dir_files:
        if (".txt" in file):
            continue
        if (".DS_Store" in file):
            continue
        n_tweets+=1
        if (""+file+" - followers.txt" in dir_files):
            n_followers+=1
        if (""+file+" - friends.txt" in dir_files):
            n_friends+=1

print("Number of tweets: "+str(n_tweets))
print("Number of followers: "+str(n_followers))
print("Number of friends: "+str(n_friends))
percentage=(n_followers+n_friends)/(2*n_tweets)
print("Percentage: "+ str(percentage))
