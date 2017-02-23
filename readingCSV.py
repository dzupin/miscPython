import csv

csvfile = open('readingCSV.py', 'rt')
reader = csv.reader(csvfile)
for row in reader:
    print (row)
