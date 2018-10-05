class A (Exception):
	pass

class b:
	def m1(self,rat):
		self.m2(rat)
	def m2(self,pin):
		if(pin==3456):
			print("a vaild number")
		else:
			self.m3()
	def m3(self):
		try:
			raise A("incorrrect PIN")
		except A as a:
			print (a)



r=b()
r.m1(37)

			

		

