import numpy as np

from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB
# Try to import a kNN classifier ;)
from sklearn.neighbors import KNeighborsClassifier

from sklearn.pipeline import Pipeline

from sklearn import metrics

from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer
from nltk import word_tokenize


######################################################################
######################################################################
######################################################################



stemmer = EnglishStemmer()

def stemming_tokenizer(text):
	stemmed_text = [stemmer.stem(word) for word in word_tokenize(text, language='english')]
	return stemmed_text

# Import the LABELED dataset...
data_folder = "./training_set"
dataset = load_files(data_folder)

print("")
print("----------------------")
print("Dataset:")
print("")
print("Total number of documents: %d" % len(dataset.data))
print("")
print("Classes:")
print(dataset.target_names)
print("----------------------")
print("")


# Split the dataset in TRAINING and TEST set:
docs_train, docs_test, Y_train, Y_test = train_test_split(dataset.data, dataset.target, test_size=0.25)
target_names = dataset.target_names

print("")
print("----------------------")
print("Creating Training Set and Test Set")
print("")
print("Training Set Size")
print(Y_train.shape)
print("")
print("Test Set Size")
print(Y_test.shape)
print("----------------------")

# Conversion of the Training Set
#count_vect = CountVectorizer("")

vectorizer = TfidfVectorizer(strip_accents= None, preprocessor = None, tokenizer=stemming_tokenizer)

#X_train_counts = count_vect.fit_transform(docs_train)
#print("")
#print("----------------------")
#print("Training Set conversion:")
#print("")
#print("NumOccurrences Documents X Terms Matrix Representation of Training Set")
#print(X_train_counts.shape)
#print("")
#tfidf_transformer = TfidfTransformer("")
X_train_tfidf = vectorizer.fit_transform(docs_train)
print("")
print("Tf-idf Documents X Terms Matrix Representation of Training Set")
print(X_train_tfidf.shape)
print("----------------------")
print("")


# Let's train a Naive-Bayes-Classifier using the Training Set.
print("")
print(" Start Learning...")
classifier = MultinomialNB().fit(X_train_tfidf, Y_train)
#classifier= KNeighborsClassifier(n_neighbors=25, weights="distance").fit(X_train_tfidf, Y_train)
print(" End Learning.")
print("")

### Classifier Evaluation

# Conversion of the Test Set in a Tf-idf format
#X_test_counts = count_vect.transform(docs_test)
X_test_tfidf = vectorizer.transform(docs_test)
print("")
print("----------------------")
print("Tf-idf Documents X Terms Matrix Representation of Test Set")
print("Documents X Terms")
print(X_test_tfidf.shape)
print("----------------------")

# Use the trained classifier to classify all documents in the Test-Set.
Y_predicted = classifier.predict(X_test_tfidf)


# Evaluate the performance of the classifiers.
output_classification_report = metrics.classification_report(Y_test, Y_predicted, target_names=dataset.target_names)

print("")
print("----------------------------------------------------")
print(output_classification_report)
print("----------------------------------------------------")
print("")

# Compute the confusion matrix
confusion_matrix = metrics.confusion_matrix(Y_test, Y_predicted)
print("Confusion Matrix: True-Classes X Predicted-Classes")
print(confusion_matrix)
print("")
print("")
