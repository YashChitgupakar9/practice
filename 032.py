import re 
Mammals = ("1 dolphin one of the few mammals that live in the sea, 2 Bear the mammal, 3 Lion king of the jungle, 4 Rodents the smallest mamammals, 5 Hynea a scavenger mammal ")
yash = re.findall("[a-z]+[A-Z]",Mammals)
alexa = re.findall("\d",Mammals)
rome  = re.findall("\w",Mammals)
print(rome)
print(alexa)
print(yash) 

f = "iInform INFORM 13 234"

match = re.findall('iI',f)
print(match)