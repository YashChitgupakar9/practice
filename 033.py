Family = ''' Yash age is 16 and gender is male Rishab age 11 and gender is male Aarti age is 42 and gender is female Millnd age is 43 and gender is male '''

import re

ages = re.findall(r'\d{2}',Family)
names = re.findall(r'[A-Z][a-z]*', Family)
gender = re.findall(r'[a-z]*ale',Family)

print (gender)

print (ages)
print (names)

a={}
x=0
y=0
for each in names:
	a[each]= "Age: " + ages[x] + " Gender: " + gender[y]
	x= x+1
	y = y+1
print(a)
print(a["Yash"])	


