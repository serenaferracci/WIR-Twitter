import os

training_set_folder="training_set"

for directory in os.listdir("Tweets"):
    if (".txt" not in directory) and ("DS_Store" not in directory):
        for file in os.listdir("Tweets/"+directory):
                if ("DS_Store" not in file) and ("followers.txt" not in file) and ("friends.txt" not in file):
                    classification="";
                    if "Society" in directory:
                        classification="Society"
                    elif "Event" in directory:
                        classification="Event"
                    elif "Health" in directory:
                        classification="Health"
                    elif "Movie" in directory:
                        classification="Movie"
                    elif "Music" in directory:
                        classification="Music"
                    elif "Politics" in directory:
                        classification="Politics"
                    elif "Science" in directory:
                        classification="Science"
                    elif "Sport" in directory:
                        classification="Sport"
                    else:
                        continue

                    in_file=open("Tweets/"+directory+"/"+file, "r");
                    out_file=open(training_set_folder+"/"+classification+"/"+file, "w");
                    all="";
                    for line in in_file:
                        all+=line;
                    out_file.write(all);
                    in_file.close()
                    out_file.close()
