# Extract the most important terms from each document


from __future__ import division
import csv
from math import log


# (Max) number of the most important terms
TERMS_NEEDED = 5

INPUT_FILE = 'train-sklearn.csv'
OUTPUT_FILE = 'tf-idf.csv'


def compute_ifidf(terms, num_documents, raw_idf, max_raw_frequency):
    """ Computes TF-IDF
        http://en.wikipedia.org/wiki/Tf%E2%80%93idf
    """
    tf_idf = dict()
    for term, frequency in terms:
        tf = 0.5 + (0.5 * frequency) / max_raw_frequency
        idf = log(num_documents/raw_idf[term])
        tf_idf[term] = tf * idf

    return tf_idf


def max_raw_frequency(terms):
     """ terms = [['a', 5], ['b', 7], ['c', 3]]
         maximum_raw_frequency(terms) => returns 7
     """
     max = 0
     for term, frequency in terms:
        if frequency > max:
             max = frequency

     return max


def extract_terms(document):
    """ document = "545,32 8:1 18:2"
        extract_terms(document) => returns [[8, 1], [18, 2]]
    """
    terms = [item.split(':') for item in document.split() if item.find(':') >= 0]
    terms = [[int(term), int(frequency)] for term, frequency in terms]
    return terms


def extract_classes(document):
    """ document = "545,32 8:1 18:2"
        extract_classes(document) => returns "545,32"
    """
    return document.split()[0]


def extract_most_important(tf_idf, terms_needed):
    """ tf_idf = {'a': 2, 'b': 0.5, 'c': 3, 'd': 1}
        extract_most_important(tf_idf, 2) => returns "c:3 a:2"
        extract_most_important(tf_idf, 3) => returns "c:3 a:2 d:1"
    """
    sort_by_value = sorted(tf_idf, key=tf_idf.get, reverse=True)
    most_important = sort_by_value[:terms_needed]
    return ' '.join([str(item) + ":" + str(tf_idf[item]) for item in most_important])



# Read IDF data

raw_idf = dict()
with open('idf.csv', 'r') as idf_data:
    reader = csv.reader(idf_data)
    for row in reader:
        raw_idf[int(row[0])] = int(row[1])


# Number of documents in the input file
from subprocess import check_output
num_documents = int(check_output(['wc', '-l', INPUT_FILE]).split()[0])


# For each document:
# 1) Compute TF-IDF
# 2) Write down T most important terms
#    into a separate file (tf-idf.csv)

with open(INPUT_FILE, 'r') as input_file:

    with open(OUTPUT_FILE, 'w') as output_file:

        for document in input_file:

            terms = extract_terms(document)
            tf_idf = compute_ifidf(terms, num_documents, raw_idf, max_raw_frequency(terms))
            most_important_terms = extract_most_important(tf_idf, TERMS_NEEDED)

            classes = extract_classes(document)
            output_file.write(classes + " " + most_important_terms + "\n")
