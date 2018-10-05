worldleaders = "primeminister of INDIA is Modi and his age is 67 , primeminister of the UNITEDKINGDOM is May and her age is 61, primeminister of FRANCE is Macron and his age is 40, primeminister of GERMANY is Merkel and her age is 63"

import re 
countries = re.findall("[A-Z][A-Z][A-Z]*",worldleaders)
leaders = re.findall("[A-Z][a-z][a-z]*",worldleaders)
post = re.findall("[a-z]*ster",worldleaders)
age = re.findall("\d{2}",worldleaders)

c =[]
c.extend(countries)
print(c)
l=[]
l.extend(leaders)
p=[]
p.extend(post)


a =[]
a.extend(age)
d={}
x=0
z=0
y=0
for each in c:
	d[each] = l[x] , "Age is " + a[y] , "and is the " + p[z]
	z=z+1
	x=x+1
	y=y+1
print(d)	







	