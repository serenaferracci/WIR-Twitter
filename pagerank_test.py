import os
import networkx as nx

pagerank_test_folder="pagerank_test"

dic={} #it will contain [folder]:[classification]

for folder in os.listdir(pagerank_test_folder):
    G = nx.DiGraph();
    for file in os.listdir(pagerank_test_folder+"/"+folder):
        if ("DS_Store" not in file) and (".txt" not in file):
            if (file+" - followers.txt" in os.listdir(pagerank_test_folder+"/"+folder)) and (file+" - friends.txt" in os.listdir(pagerank_test_folder+"/"+folder)):
                if int(file) not in G:
                    G.add_node(int(file))
                friends_file=open(pagerank_test_folder+"/"+folder+"/"+file+" - friends.txt", "r");
                for line in friends_file:
                    if int(line.strip()) not in G:
                        G.add_node(int(line.strip()))
                    G.add_edge(int(file), int(line.strip()))
                friends_file.close();
                followers_file=open(pagerank_test_folder+"/"+folder+"/"+file+" - followers.txt", "r");
                for line in followers_file:
                    if int(line.strip()) not in G:
                        G.add_node(int(line.strip()))
                    G.add_edge(int(line.strip()), int(file))
                followers_file.close();
    pagerank=nx.pagerank(G)
    top_100=[]
    if len(pagerank)>100:
        top_100 = sorted(pagerank, key=pagerank.get, reverse=True)[:100]
    else:
        top_100 = sorted(pagerank, key=pagerank.get, reverse=True)
    out=open(pagerank_test_folder+"/"+folder+"/topk.txt", "w")
    for elem in top_100:
        out.write(elem+"\n")


    
