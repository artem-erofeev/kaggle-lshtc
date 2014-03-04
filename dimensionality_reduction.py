from sklearn.datasets import load_svmlight_file
from sklearn.decomposition import TruncatedSVD

X_train, y_train = load_svmlight_file("train-sk-min.csv", multilabel=True)
X_test, y_test = load_svmlight_file("test-sk-min.csv", multilabel=True)


# Truncated SVD, also known as Latent Semantic Analysis (LSA)
# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html

svd = TruncatedSVD()
X_train_reduced = svd.transform(X_train)
