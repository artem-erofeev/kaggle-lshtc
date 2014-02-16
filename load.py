from sklearn.datasets import load_svmlight_file
from sklearn.naive_bayes import MultinomialNB #GaussianNB

#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.svm import LinearSVC
from numpy import shape

X_train, y_train = load_svmlight_file("train-sk-min.csv", multilabel=True)
X_test, y_test = load_svmlight_file("test-sk-min.csv", multilabel=True)

##print shape(X_test), shape(y_test)
#X_train = X_train.toarray()
#X_test = X_test.toarray()

gnb = MultinomialNB()
gnb = gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)	



print("Number of mislabeled points : %d" % (y_test != y_pred).sum())