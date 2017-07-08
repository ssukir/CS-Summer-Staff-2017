import csv
import pandas

csvfile = open('jun8.csv')

reader = csv.reader(csvfile)

df = pandas.read_csv(csvfile)
timestamp = df['Timestamp']

DATA = []

for columns in reader:
  DATA += [ columns ]

# print("DATA is", DATA[0:1])
print (timestamp)

csvfile.close()
