import re
reptiles = ("CrocOdile is the largest species of reptile, while Snakes are the most venomous, YASH frogs are the smallest, Komodo dragon is the largest land reptile"  )
matches = re.findall('[a-z]*',reptiles)

#print (matches)

# re is a module (regular Expressions) and findall() is method in it. 
# findall(expression, target string)... expression must be in the format of String.. + 

