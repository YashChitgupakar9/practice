#class Test:
#	def __init__(self):
#		raise ZeroDivisionError()

#Test()

class My_Own_Error(Exception):
	def __init__(self):
		print ("Invalid Operation")


class Example:
	def __init__(self):
		raise My_Own_Error();
try:
	Example()
except:
	print ("Please careful while operating your account")