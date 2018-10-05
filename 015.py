c =["hyderabad","kolkata","Mumbai","mohali","chennai","shimla"]
f =["biryani","rasgulla","vadapav","butterchicken","idly","apples"]
s =["charminar","marble palace","gateway of india","pca","madra university","gortons castle"]


ref ={}
x=0
for each in c:
	ref[each] = f[x],s[x]
	x=x+1
print(ref['shimla'])
print("kolkata" in ref )
print(ref)


Details = {1: {'name': "Yash", "Hobbies": "Adventure", "Qual": "11th Standard"}, 2:{"Name":"Rishab", "Hobbies":"Lego", "Qual": "7th Standard", "interests": "Pygames"}, 3:{"Name":"Aarthi", "Qual": "Masters"}, 4: {"Name":"Millnd", "Qual": "Masters"}}

#print (Details[1]['name'])

for each, data in Details.items():
	#print ("\nSequence Number: ", each)
	for info in data.items():
		pass
		#print (info)\

		
print(c.index("mohali"))