class yash:
	def method1(self):
		self.method2()
	def method2(self):
		self.method3()
		
			
		
	
	def method3(self):
		print(10/2)
		print(10/0)

y=yash()
try:
	y.method1()
except:
	print(305//3)
else :
	print("its correct")






		
