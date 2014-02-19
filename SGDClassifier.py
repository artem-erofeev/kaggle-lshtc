from sklearn.datasets import load_svmlight_file
X_train, y_train = load_svmlight_file("train-sklearn.csv", multilabel=True)
X_test, y_test = load_svmlight_file("test-sklearn.csv", multilabel=True)

from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Number of mislabeled points : %d" % (y_test != y_pred).sum())
