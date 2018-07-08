Web Information Retrieval Project (A.Y. 2017/2018)

Written by Maria Ludovica Costagliola, Emanuele De Santis and Serena Ferracci

In this project we try to classify Twitter Trending Topics using two main approaches:
* Naive Bayes Classifier on tweets text
* PageRank on users' graph

In the first case we vectorize the documents using TF-IDF. We try to combine also a stemmer from nltk
but some tweets are not in English and often tweets are written in slang.

In the second case we obtain only a theoretical result because the graph to build is too big to fit in main memory
(it uses more than 24GB RAM)
