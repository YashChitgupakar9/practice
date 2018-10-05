sample = "From: To Whom: "

import re 

match = re.findall(r'^F.*?:',sample)
print (match)

s = "From: yashddragon@gmail.com To Whom: "

s1 = re.findall("[a-z]*@[a-z]*.com",s)

print(s1)

s2 = re.findall(r'\S+@\S+',s)
print (s2)

s3 = s.find("@")
print (s3)

s4 = s.find(' ',s3)
print (s4)

s5 = s.find('y')
print (s5)

s6 = s[6:28]
print (s6)