def perform(x,y):
	if(x == y):
		print (x+y)
	elif (x>y):
		print (x*y)
	else:
		print (x-y)
#print (__name__)
global_variable = "global_variable"
class First_Class:
	def __init__(self):
		print ("First_Class Object...")
		self.instance_variable = "FirstClass"		# instance or non-static variables...  

	def first_method(self):			# instance method... or non-static method. 
		return "its first method"
		local_variable = "local variable"

	def first_class_method():		# class or static method
		return " first class method..."

	class_variable = 10			# class variable or static variable.. or non-instance variable

if __name__ == '__main__':
	perform(2,39)
	f = First_Class()
	f.first_method()