eulan=[['london','english'],['madrid','spanish'],['berlin','german'],['paris','french'],['lisbon','portuguese'],['helsinki','finnish'],['warsaw','po.lish'],['bratislava','slovaik']]
#print (eulan[1])
for each in enumerate(eulan):
	print(each)

aslan=["hindi","mandarin","cantanese","japanease","arabic","mongolian","russain"]
for each in enumerate(aslan):
	print (eulan[0][1])
#eulan.extend(aslan)
#print(eulan)
countries = ["united kingdom","spain" ,"germany","France","portugal","finland", "Slovakia", "Poland"]

#Data = {countries[0]:eulan[0], countries[1]:eulan[1], countries[2]:eulan[2]}


y = 0

diction = {}

for each in countries:
	diction[each] = eulan[y]
	y = y+1

print (diction)