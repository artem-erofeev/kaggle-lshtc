import csv

def number_of_features(filename):

    max = 0

    with open(filename, 'r') as f:
        for document in f:
            terms = [int(item.split(':')[0]) for item in document.split() if item.find(':') >= 0]
            for term in terms:
                if term > max:
                    max = term

    return max


print "train-sk-min.csv:", number_of_features("train-sk-min.csv"), "features."
print "test-sk-min.csv:", number_of_features("test-sk-min.csv"), "features."
print 
print "train-sklearn.csv:", number_of_features("train-sklearn.csv"), "features."
print "test-sklearn.csv:", number_of_features("test-sklearn.csv"), "features."
