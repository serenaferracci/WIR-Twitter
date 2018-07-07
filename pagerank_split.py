import os
import math
import random
training_folder="pagerank_training"
test_folder="pagerank_test"

if not os.path.exists(training_folder):
    os.makedirs(training_folder)

if not os.path.exists(training_folder):
    os.makedirs(training_folder)

list_of_folders=[]
for directory in os.listdir("Tweets"):
    if ("DS_Store" not in directory) and (".txt" not in directory):
        list_of_folders.append(directory)
print(len(list_of_folders))
n_train=math.floor(len(list_of_folders)*0.75)
n_test=len(list_of_folders)-n_train
train=random.sample(list_of_folders, k=n_train)
test=[]
for elem in list_of_folders:
    if elem not in train:
        test.append(elem);

for dir in train:
    if not os.path.exists(training_folder+"/"+dir):
        os.makedirs(training_folder+"/"+dir)
    for file in os.listdir("Tweets/"+dir):
        if ("DS_Store" in file):
            continue;
        in_file=open("Tweets/"+dir+"/"+file, "r");
        out_file=open(training_folder+"/"+dir+"/"+file, "w");
        for line in in_file:
            out_file.write(line);
        in_file.close()
        out_file.close()

for dir in test:
    if not os.path.exists(test_folder+"/"+dir):
        os.makedirs(test_folder+"/"+dir)
    for file in os.listdir("Tweets/"+dir):
        if ("DS_Store" in file):
            continue;
        in_file=open("Tweets/"+dir+"/"+file, "r");
        out_file=open(test_folder+"/"+dir+"/"+file, "w");
        for line in in_file:
            out_file.write(line);
        in_file.close()
        out_file.close()
