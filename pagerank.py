import networkx as nx
import os

G = nx.DiGraph();
topic = "Movie"

for directory in os.listdir("Tweets"):
    if ("DS_Store" not in directory) and (".txt" not in directory) and (topic in directory):
        for file in os.listdir("Tweets/"+directory):
            if ("DS_Store" not in file) and ("followers.txt" not in file) and ("friends.txt" not in file):
                if file not in G:
                    G.add_node(int(file));
                if (file+" - friends.txt" not in os.listdir("Tweets/"+directory)) or (file+" - followers.txt" not in os.listdir("Tweets/"+directory)):
                    continue;
                friends_file=open("Tweets/"+directory+"/"+file+" - friends.txt", "r");
                for line in friends_file:
                    if line.strip() not in G:
                        G.add_node(int(line.strip()))
                    G.add_edge(int(file), int(line.strip()))
                friends_file.close();
                followers_file=open("Tweets/"+directory+"/"+file+" - followers.txt", "r");
                for line in followers_file:
                    if line.strip() not in G:
                        G.add_node(int(line.strip()))
                    G.add_edge(int(line.strip()), int(file))
                followers_file.close();

pagerank = nx.pagerank(G);
print("Twitter ID of pagerank over "+topic+": "+str(max(pagerank)))
