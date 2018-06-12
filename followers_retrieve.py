import tweepy
import json
import os
import sys
import time

NUM_USERS=6;
if (len(sys.argv)!=2):
    print("You have to specify an initial seed!")
    exit(1)

#seed value indicates which folders it selects
seed=int(sys.argv[1]) #please write an integer as parameter

#seed=0 Emanuele
#seed=1 Serena
#seed=2 Ludovica

usa_location = 23424977

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

if seed==0:
    # Emanuele's keys
    consumer_key = 	"tVyk6jPU4UPBnaGdHMCGvAY48"
    consumer_secret = "QAEViQSW6xE5wRVHwJQP8asDnwXgCmWoN06WE6ep1hgKgIPciQ"

    access_token = "841341908957954051-PSaSB6RVihZgvCz0RIlYHr3T4ZGg21E"
    access_token_secret = "VMIhfKGvVM9FRMrdq7L1Sy5xWHXid7NF7g7Mc1ZO8JxZi"
elif seed==1:
    #Serena's keys
    consumer_key = 	"MNIY1db3L8UIWbWwcIufdbLsE"
    consumer_secret = "EI9DxGIM7BoJOzNHUPjTn3kIPwK8OjNTWgLeWlb46wMg5gvFmE"

    access_token = "455678422-G3uLg4O7ulLaZbyVhaSa2zPZamyHjC6eUClw0hUC"
    access_token_secret = "gGTh7L7O5P7EhsKiqcESXqA9RXjiafNZOrc5MVXBEap4i"

elif seed==2:
    #Ludo's keys
    consumer_key="dDEH0jtYRRvXPsx55LJqF86kq"
    consumer_secret="Bt5UWBvE3gMZQkDzdCU5Iuk0gfooGxVR9dYai76WEzxhLKSnaM"

    access_token="315710007-dTyuxZoGhBGFCMrarAqt27WaYuKNSBW2P5IZKtLA"
    access_token_secret="xUqFFO3LFroFjgO5XVAW1MYkYQhHoxmyLzMAwtHFh8Do1"

elif seed==3:
    #Riccardo's key
    consumer_key = 'wgyF8eM0142tmip6dwNFNR7gl'
    consumer_secret = 'rGPAlNBF5nrSE6fofq23Bt5BwlBNpd1kLhjUofhEw2dMmoTv7V'

    access_token="1000293863163129856-GoWCSNnKiOm03b4KgrSOdkgeUcJZ99"
    access_token_secret="2QURVPydYfJfiF8u36ZS7NqfewT1QfgTfVZSSjWnQGH50"

elif seed==4:
    #Ilaria's keys
    consumer_key="CCQuRUXXwmWtKLWLvZrME5Tu3"
    consumer_secret="RPoEEiEofMZxjfzywYUoIUT8NTs1WUN5IO6ZdqmMxmBAIEhTiM"

    access_token="792629040595214336-w4Zrb1V4rycmtgltYXro3vgkdIKb9Kt"
    access_token_secret="nK7ZyfZsq9gwBgVDomvg8bfrqHQx81FRqbPjsQvE94SDr"

else:
    #Matteo's keys
    consumer_key="ETFCxxqm4tjN7xd5TIhXg2RIX"
    consumer_secret="mNIUzH4FrsRJpIc2hiMKmRIhDnDIJfTBBbRtmIRPTPW2TkNnl8"

    access_token="941832650-BHsUvRMpKh2f0e9OYCyjuGcgvZjt7j7HcCQZCsTR"
    access_token_secret="oLrFrByYqUciVE7hFB9tffhtNQqrWhh0PxygFPD97ibbB"

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

auth=tweepy.AppAuthHandler(consumer_key, consumer_secret)

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
'''
except tweepy.RateLimitError:
    print("["+time.ctime()+"] Tweets limit reached, retry in 15 minutes...")
    time.sleep(910)
    print("["+time.ctime()+"] Retry now...")
    continue;
'''
directory=os.listdir("Tweets")
i=0
for i in range(0, len(directory)):
    if ".DS_Store" in directory[i]:
        continue
    if ".txt" in directory[i]:
        continue
    if i%NUM_USERS!=seed:   #this is not your folder, please continue
        continue
    dir=directory[i]
    listdir=os.listdir("Tweets/"+dir)
    for file in listdir:
        if ".DS_Store" in file:
            continue
        if (".txt" in file):
            continue
        if ((""+file + " - followers.txt") in listdir):
            print("["+time.ctime()+"] Followers for user "+ file+" yet retrieved")
            continue
        users=tweepy.Cursor(api.followers_ids, id=file, count=800000).items()
        out_fl = open("Tweets/" + dir + "/" + file + " - followers.txt", "w")
        while True:
            try:
                print("["+time.ctime()+"] Retrieving followers for user "+file)
                for user in users:
                    out_fl.write(str(user) + "\n")
                out_fl.close()

                print("["+time.ctime()+"] Retrieved followers for user "+file)
                break
            except tweepy.TweepError as e:
                print("["+time.ctime()+"] "+e.reason);
                if("88" in e.reason):
                    status=api.rate_limit_status()
                    millis=status["resources"]["followers"]["/followers/ids"]["reset"]-int(time.time())
                    if status["resources"]["followers"]["/followers/ids"]["remaining"]==0:
                        print("["+time.ctime()+"] Still missing "+str(millis)+ " seconds")
                    if millis<0:
                    	time.sleep(300)
                    else:
                    	time.sleep(millis+1)
                    print("["+time.ctime()+"] Retry now...")
                    continue;
                break
    print("["+time.ctime()+"] End of the process, collected friends and followers!")
