class Fighter:
	def __init__(self, name):
		self.name = name	#Attribute passed in
		self.health = 100	#Global Attribute for objects
		self.damage = 10 	#Global Attribute for objects

	def attack(self, other_guy): #Define Attack Method
		other_guy.health = other_guy.health - self.damage #Apply damage to opponent health

qazi = Fighter('Qazi')
bob = Fighter('Bob')

print(qazi.name)
print(bob.name)

bob.attack(qazi)

print(qazi.health)
print(bob.health)