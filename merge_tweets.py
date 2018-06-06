import re
import os

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

tweets_folder="Tweets"

for subfolder in os.listdir(tweets_folder):
    out=open(tweets_folder+"/"+subfolder+".txt", "w");
    for file in os.listdir(tweets_folder+"/"+subfolder):
        f=open(tweets_folder+"/"+subfolder+"/"+file, "r")
        string=f.read()
        emoji_pattern.sub(r'', string) # no emoji
        out.write(string+"\n")
        f.close();
    out.close();
