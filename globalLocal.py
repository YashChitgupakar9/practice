

class Test:
	x = 10
	s = "test"
	name = "something"
	def test(self, hi):
		global x
		x = "on earth"
		self.name =  "Yash"
		print (self.name)

t = Test()
print (t.name)
print (x)
t.test("say")
print (t.name)
print (x)
print (t.x)