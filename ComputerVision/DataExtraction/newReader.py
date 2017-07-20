import csv

inputFile = csv.DictReader(open('jun8.csv'))

for row in inputFile:
    # we want to skip every 5 columns (including the first and second)
    print (row)

csvfile.close()
