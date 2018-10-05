import csv

f = open("SampleMedicine.csv")

yash = csv.reader(f)


for each in yash:
	print (each[0])