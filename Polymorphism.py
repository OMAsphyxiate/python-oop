class Animal:
	def __init__(self, name):
		self.name = name

	def talk(self):
		pass	#pass means do nothing




pet_qazi = Animal("Qazoo") #Uses Animal class to set pet_qazi object with value for Animal.name = Qazoo
print(pet_qazi.name) #Should print Qazoo
print(pet_qazi.talk())


class Dog(Animal):
	def talk(self): #Example of Polymorphism, since talk method already exists in the Animal class, this method takes over for the Dog class
		return "WOOF"

class Cat(Animal):
	def talk(self):
		return "MEOW"


pet_dog = Dog("Dot")
print(pet_dog.name)
print(pet_dog.talk())

pet_cat = Cat("Icarus") #Create new cat named Icarus, since the Cat class is inheriting from Animal which looks for the Name argument
print(pet_cat.name)
print(pet_cat.talk())