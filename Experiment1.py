import re

s = "Hello, inform him with the latest information"

m = re.findall(pattern='inform',string=s)
#print (m)

tele_num= "123 456 7890, (124) 234 2345, 123123 1234, +91 (234) 234 2345, 1800 235 5666, 1 23 23 23434"
m1 = re.findall('\s?\+?9?1?\s?\(?\d{1,4}\)?\s?\d{2,3}\s\d{1,4}\s\s\d{5}?',tele_num)
print (m1)

m2 = re.match(r'[A-Z][a-z]*',s)
#print (m2)
m3 = re.findall(r'm([A-Za-z0-9]*)',s)
#print (m3)
m4 = re.findall(r'^Hello',s)

print (m4)
