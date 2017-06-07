class BankAccount:
	def __init__(self, account_type, amount):
		self.account_type = account_type
		self.amount = amount


	def deposit(self, deposit_amount):
		self.amount += deposit_amount #Sets the amount value of the object equal to the SUM of account and the deposit

	def withdraw(self, withdraw_amount):
		self.amount -= withdraw_amount #Sets the amount to current Amount minus the Withdraw

	def __str__(self):
		return "{} Amount: {}".format(self.account_type, self.amount)


qazi = BankAccount("Checkings", 100) #Declares qazi object using the BankAccount class

print(qazi.account_type) #Should return Checkings
print(qazi.amount) #Should return current amount of 100

qazi.deposit(30) #Uses method deposit to add 30
print(qazi.amount) #Should return 130 with the new deposit added

qazi.withdraw(45)
print(qazi)
print(qazi.amount)