class Animal:

	def eat(self):
		return "i am a generic eat method";

	def walk(self):
		return "i m generally defined how ot walk.. "

	def instinct(self):
		return "the character which defines a species"


class Dog(Animal):
	def eat(self):
		return "it eats pedigree"
	def breed(self):
		return "golden retriver"
		return "labodore"


# 	Dog IS-A Animal ; Dog has a characteristics of an Animal
# Animal HAS Dog		





d=Dog()
print(d.eat())
print(d.walk())
print(d.breed())

class germanshepard(Dog,Animal):
	print(d.eat())


g = germanshepard()
print (g.instinct())






