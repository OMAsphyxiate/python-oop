import datetime #Imports the datetime Library

setDate = datetime.date(2015, 7, 14) #Creates object from the class datetime.date()

print(setDate)
print(datetime.date.today()) #Shows current date
print(datetime.date.today().year) #Shows current year
print(datetime.date.today().month) #Shows current month
print(datetime.date.today().day) #Shows current day


class Age: #Define Age class

	def __init__(self, year, month, day):
		self.birthday = datetime.date(year, month, day)
		self.days = datetime.date.today() - datetime.timedelta(days=birthdate)

	def __str__(self):
		return"You are {} days old".format(self.days)


birthday1 = Age(2010, 1, 30)
birthday2 = Age(1986, 10, 6)
birthday3 = Age(2000, 5, 15)



print(birthday1)
print(birthday2)
print(birthday3)