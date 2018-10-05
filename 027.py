class A:

	def m1(self):
		self.name = "A";
		print (self.name)
		return "Its just Initializing";

	def m2(self):
		self.property = "nothing"


a = A()

print (a.m1())
print (a.m2())