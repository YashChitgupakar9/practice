import csv

f = open("C:/Users/om sai/Desktop/SampleData.csv")

csv_f = csv.reader(f)
next(csv_f)

Details = []

for each in csv_f:
	print (each)

#print (Details[0][0])

print (type(Details))