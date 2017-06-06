class Fighter:
	def __init__(self, name):
		self.name = name	#Attribute passed in
		self.health = 100	#Global Attribute for objects
		self.damage = 10 	#Global Attribute for objects

	def attack(self, other_guy): #Define Attack Method
		other_guy.health = other_guy.health - self.damage #Apply damage to opponent health
		print("{} attacks {}!".format(self.name, other_guy.name))
		print("{} loses {} health".format(other_guy.name, self.damage))
		#Prints out the attack using the variable injection into string

	#Changes how the print function interacts when printing an Object
	def __str__(self): #dunder method (double underscore on both sides)
		return "{}: {}".format(self.name, self.health)
		#injects the two passed variables into the brackets {} (place holder) within the string

qazi = Fighter('Qazi')
bob = Fighter('Bob')

print(qazi)	# <__main__.Fighter object at 0x00000207C22C22B0> before __str__ formatting
print(bob)

bob.attack(qazi)

print(qazi)
print(bob)