import datetime #Imports the datetime Library

class Age: #Define Age class

	def __init__(self, year, month, day):
		self.birthday = datetime.date(year, month, day)
		self.today = datetime.date.today()
		self.days = self.today - self.birthday

	def __str__(self):
		return"You are {} days old".format(self.days)

birthyear = input("Please enter your birth year: ")
birthmonth = input("Please enter your birth month: ")
birthday = input("Please enter your birth date: ")

UserInput = Age(int(birthyear), int(birthmonth), int(birthday))

print(UserInput)