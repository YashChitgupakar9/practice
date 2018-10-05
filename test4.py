import csv

f = open("SampleMedicine.csv")

#print (f)

yash = csv.reader(f)
next(yash)
list1 = []
list2 = []
for each in yash:
	#print (each)
	list1.append(each[0])
	list2.append(each)

list3= []
for each in list2:
	s = each[1] + each[2] +each[3]+ each[4]
	list3.append(s)
#print (list3)

diction= {}
x =0
for each in list1:
	diction[each] = list3[x]
	x = x+1;

print (diction["ADNI (Alzheimer's Disease Neuro-Imaging Initiative)"])