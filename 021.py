try:
	print (10/0)
	
except ZeroDivisionError:
	print(37//3)
except FileNotFoundError:
	print ("file is not exist")
else:
	print ("statement 1")
	print ("statement 2")
finally:
	print ("i always execute.. ")

try:
	f = open("Sample.txt")
except:
