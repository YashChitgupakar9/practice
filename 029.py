class Football:
	
	# pass doesn't do anything. its just like a statement.. instead keep class as an empty, if you do wish to have any statements in class, then you keep 'pass'

	def __init__(self, x):
		print (x)

	def condictions(self):
		print ("FIFA rules...")



Football(23749)
#1. Whenever you create an object, It is going to call a Constructor of that same class. 
#2. Implicity there is a constructor for every class that you write it. 
#3. at the time of creating an Object, if you are not passing any arguments, then it invokes default constructor provided by Python Intepreter...
#4. What is the Python Interpreter provided constructor looks like:
				#   def __init__(self):
						# super().__init__()
						#  "super" is a keyword which always refers to superclass object
# 5. If you have any other requirement immediately after creation of an Object, then you can create your own constructor. 
# 6. Constructor name must be always def __init__(self, )
# 7. If you have created your own constructor, Python Intepreter doesnt or never ever provides you another constructor. 
# 8. Constructors never be called explicitly
# 9. Whenever you create an Object, it is going to call/invoke call the constructor of that same class.. That constructor must have to call implicitly  super class constructor. 
#10. 

