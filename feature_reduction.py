# Reduce the dimension of the feature vector.

# This script works with tf-idf.csv (produced by tf-idf.py),
#   where each document is represented with 5 most important features.

# The task of this script:
#   leave only the features that are mentioned at least once.
#   Renumber them as 1, 2, 3, 4 etc.


INPUT_FILE = 'tf-idf.csv'


def parse(document):
    """ Parse the document string to get the data.
        doc = "1,3,17 5:8.03 6:6.33 79:4.47"
        => returns ("1,3,17", [5, 6, 79], [8.03, 6.33, 4.47])
    """
    raw_parse = document.split()
    classes = raw_parse[0]

    features_and_values = [item.split(':') for item in raw_parse[1:]]
    features = [int(item[0]) for item in features_and_values]
    values = [float(item[1]) for item in features_and_values]

    return classes, features, values


def compose(classes, features, values):
    """ Opposite to parse: Compose the document string knowing the data.
        classes = "1,3,17"; features = [1, 2, 3]
        values = [8.03, 6.33, 4.47]
        => returns "1,3,17 1:8.03 2:6.33 3:4.47"
    """
    features_and_values = ' '.join([str(features[i]) + ":" + str(values[i]) for i in range(len(features))])
    return ' '.join([classes, features_and_values])

