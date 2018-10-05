import urllib.request
import re
url = "https://www.summet.com/dmsi/html/codesamples/addresses.html"
clim = urllib.request.urlopen(url)
r = clim.read()
dutch = r.decode()
people = re.findall("\<li>([A-Z][A-Za-z]*\s[A-Z][a-z]*)",dutch)

#print(people)
print(len(people))
places = re.findall("\<br\/\>([\w\s#-.]+)",dutch)
#print(len(places))
#print(places)
x = 0
y = 1
z = 2
addresses = []
phones = []
for each in range(100):
	addresses.append(places[x] + " "+places[y])
	phones.append(places[z])
	x = y+1
	y = y+2
	z= z+3
print(len(addresses))
print (len(phones))
#print(l)

d = {}
s = 0
p = 0


for each in people:
	d[each] = "address : " + addresses[s] + " " "phone number : " + phones[p]
	s = s+1
	p = p+1
print(d["Calista Wise"])
d1 = {}	
c = 0
v =0


for each in phones:
	d1[each] = "name : " + people[c] + " " "address : " + addresses[v]
	c = c+1
	v = v+1
print(d1["(404) 960-3807"])	







