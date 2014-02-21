# Extract the most important terms from each document


import csv
from math import log
from __future__ import division

# (Max) number of the most important terms
T = 5

# Read IDF data

raw_idf = dict()
with open('idf.csv', 'r') as idf_data:
    reader = csv.reader(idf_data)
    for row in reader:
        raw_idf[int(row[0])] = int(row[1])


# A function to compute TF-IDF
# http://en.wikipedia.org/wiki/Tf%E2%80%93idf


def compute_ifidf(terms, num_documents, max_raw_frequency):

    tf_idf = dict()
    for term, frequency in terms:
        tf = 0.5 + (0.5 * frequency) / max_raw_frequency
        idf = log(num_documents/raw_idf[term])
        tf_idf[term] = tf * idf

    return tf_idf


# For each document:
# 1) Compute TF-IDF
# 2) Write down T most important terms
#    into a separate file (tf-idf.csv)

with open('train-sk-min.csv', 'r') as input_file:
    num_documents = reader.line_num

    with open('tf-idf.csv', 'w') as output_file:
        writer = csv.writer(output_file, delimiter=',', lineterminator='\n')

        for document in input_file:

            terms = [item.split(':') for item in document.split() if item.find(':') >= 0]
            terms = [[int(term), int(frequency)] for term, frequency in terms]

            max_raw_frequency = 0
            for term, frequency in terms:
                if frequency > max_raw_frequency:
                    max_raw_frequency = frequency

            tf_idf = compute_ifidf(terms, num_documents, max_raw_frequency)

            sorted_keys_ascending = sorted(tf_idf, key=tf_idf.get)
            # T_most_important_terms = sorted_keys_ascending[-T:]
            # ... stopped here
