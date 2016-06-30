import csv

csvfile = open('readingCSV.py', 'rb')
reader = csv.reader(csvfile)
for row in reader:
    print row
