import string

from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer
from nltk import word_tokenize

from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from sklearn import metrics

import pprint as pp


######################################################################
stemmer = EnglishStemmer()

def stemming_tokenizer(text):
	stemmed_text = [stemmer.stem(word) for word in word_tokenize(text, language='english')]
	return stemmed_text
######################################################################



## Dataset containing Positive and neative sentences on Amazon products
data_folder_training_set = "./Tweets_train"
data_folder_test_set     = "./Tweets_test"

training_dataset = load_files(data_folder_training_set)
test_dataset = load_files(data_folder_test_set)
print("")
print("----------------------")
print(training_dataset.target_names)
print("----------------------")
print("")


# Load Training-Set
X_train, X_test_DUMMY_to_ignore, Y_train, Y_test_DUMMY_to_ignore = train_test_split(training_dataset.data,
													training_dataset.target,
													test_size=0.0)
target_names = training_dataset.target_names

# Load Test-Set
X_train_DUMMY_to_ignore, X_test, Y_train_DUMMY_to_ignore, Y_test = train_test_split(test_dataset.data,
													test_dataset.target,
													train_size=0.0)

target_names = training_dataset.target_names
print("")
print("----------------------")
print("Creating Training Set and Test Set")
print("")
print("Training Set Size")
print(Y_train.shape)
print("")
print("Test Set Size")
print(Y_test.shape)
print("")
print("Classes:")
print(target_names)
print("----------------------")


# Conversion of the Training Set
count_vect = CountVectorizer("")
X_train_counts = count_vect.fit_transform(X_train)
print("")
print("----------------------")
print("Training Set conversion:")
print("")
print("NumOccurrences Documents X Terms Matrix Representation of Training Set")
print(X_train_counts.shape)
print("")
tfidf_transformer = TfidfTransformer("")
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print("")
print("Tf-idf Documents X Terms Matrix Representation of Training Set")
print(X_train_tfidf.shape)
print("----------------------")
print("")


## classifier
print("")
print(" Start Learning...")
classifier = MultinomialNB().fit(X_train_tfidf, Y_train)
print(" End Learning.")
print("")
