w=[[["europe"],["spain","england","germany","italy","france"]],[["southamerica"],["brazil","argentina","columbia","bolivia","peru"]],[["northamerica"],["unitedstates","mexico","canada","greenland","hondurus"]]]

z = []
x = []
for each in w:
	z.append(each[0])
	x.append(each[1])

print (z)
print (x)

diction = {}
b =0
c= 0
for each in z:
	diction[each[0]] = x[b]
	b = b+1
print (diction)

print(dict([(1,2),(1,3),(2,3)]))


