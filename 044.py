class Test:
	def __init__(self):
		#nreturn "constructor"
		# Constructors Never Ever has a return statement. 
		print ("heelloooooooooo")

	def m1(self):
		return "m1 method. "

	def m2(self):
		print ("m2 method")
		return "m2 again"


t = Test()
print (t.m1())
print (t.m2())
