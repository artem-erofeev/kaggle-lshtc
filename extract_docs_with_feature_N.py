# For each feature with IDs between 1 and 1000
# extract IDs of documents that contain these features.

INPUT_FILE = 'train-sklearn.csv'
NR_FEATURES = 1000

# assign an empty set of documents for each feature
documents = dict()
for feature in range(1, NR_FEATURES + 1):
    documents[feature] = set()          
            
from feature_reduction import parse

document_id = 1

with open(INPUT_FILE, 'r') as input_file:

    for document in input_file:
         terms = parse(document)
         # to be continued



