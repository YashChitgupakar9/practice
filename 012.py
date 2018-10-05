d ={1:"yash",2:"rishab",3:"aarti",4:"milind"}

d[5] = "vihan"	
for each in d:
	print(each, d[each])

e ={'kkr':'karthik',"csk": "dhoni","rr":"smith","srh": "willamson","rcb": "kohli","kxip": "ashwin"}
print(e["srh"])
print(e.get("csk"))
#print(dir(e))
#print(help(e.fromkeys))

listings = ["English", "Maths", "Science", "Programming"]

values = [43,63,63,53] 

s = {}.fromkeys(["English","maths",'science','programmimg'], values)
print (s)

d1 = dict({1:"hi", 2:"hey", 3:"hello"})
print (d1)

d2 = dict([(1, "SRH"),(2, "CSK"),(3, "KKR")])

print (d2)