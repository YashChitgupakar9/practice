worldcup = "Germany  is from europe and has 4 titles, Spain is from europe and has 1 titles, Brazil is from southamerica ande has 5 titles, Argentina is from southamerica and has 2 titles"

import re 
countries = re.findall("[A-Z][a-z]*",worldcup)
yash = re.findall("\d",worldcup)
trophies = re.findall("[a-z]*tles",worldcup)
continents = re.findall("[a-z]*ope",worldcup)
print(continents)
print(yash)
print(trophies)




g={}
g[countries[0]] = (countries[0] , yash[0], trophies[0], "1954,1974,1990,2014")
print(g["Germany"])
print (g)
d={}

x=0
y=0	

for each in countries:
	d[each] = "1954-2014: " + yash[x] , trophies[y]
	x=x+1
	y=y+1
print(d)	