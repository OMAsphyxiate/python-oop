#Create a class called Person
#Create INIT method
#Pass 2 attributes to class
#create object from Person class
import datetime

class Person: #Define Person class
	def __init__(self, name, birthdate): #Pass two attributes name and birthdate
		self.name = name
		self.birthdate = birthdate

	def age(self):
		today = datetime.date.today()
		age = today.year - self.birthdate.year #Current year - birth year
		return age

christian = Person('Christian', datetime.date(1986, 10, 6)) #Create new object 'christian' with name of 'Christian' and birthdate of '10/6/1986' in a datetime format
print(christian.name) #Print the name attribute from the `christian` object
print(christian.birthdate) #Print the birthdate attribute from the `christian` object
print(christian.age()) #Print age of `christian` object
