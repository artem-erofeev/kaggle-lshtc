from collections import defaultdict
import csv

count = defaultdict(int)

with open('train-remapped.csv', 'r') as f:
    for document in f:
        terms = [item.split(':')[0] for item in document.split() if item.find(':') >= 0]
        for term in terms:
            count[int(term)] += 1

##for item in sorted(count):
##	print item, ' => ', count[item]


writer = csv.writer(open("output.csv", "w"), delimiter=',', lineterminator='\n')
for item in sorted(count):
    writer.writerow([item, count[item]])	
