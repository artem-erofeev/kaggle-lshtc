### Data preprocessing script
  
# Prepare the data for sklearn.datasets.load_svmlight_file
#
#   - delete the first line (http://stackoverflow.com/q/339483)
#   - delete spaces between class labels

tail -n +2 train-remapped.csv | sed "s/, /,/g" > train-sklearn.csv
tail -n +2 test-remapped.csv | sed "s/, /,/g" > test-sklearn.csv

# Prepare smaller files to play with

head -1000 train-sklearn.csv > train-sk-min.csv
head -1000 test-sklearn.csv  > test-sk-min.csv
