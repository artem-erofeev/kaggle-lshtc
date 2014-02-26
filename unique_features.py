# Count unique features
INPUT_FILE = 'tf-idf.csv'

from feature_reduction import parse

unique_features = set([])

with open(INPUT_FILE, 'r') as input_file:

    for document in input_file:
        classes, features, values = parse(document)
        [unique_features.add(feature) for feature in features]

print "Number of unique features:", len(unique_features)
