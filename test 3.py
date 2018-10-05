x_value = 10
print(x_value)
def my_function(self):
	print (self)

def function2(self,  x_value):
	print (x_value)

class Test:
	x_value = 20
	print (x_value)

	def a_method(self):
		print (self.x_value)

	def method2(self, x_value):
		x_value = 30
		print (x_value)
	print (x_value)
print(x_value)


my_function("yash")
function2("Rishab",90)


t=Test()
t.a_method()
t.method2(25)