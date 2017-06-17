#Create a class called Person
#Create INIT method
#Pass 2 attributes to class
#create object from Person class
import datetime
import tkinter as tk #Import and alias tkinker library as tk


#Create Tk object
window = tk.Tk()

#Set frame size
window.geometry("400x400") 

#Set the display name of the frame/window
window.title("AGe Calculator App!") 

#Adding labels
year_label = tk.Label(master=window, text="Year")
year_label.grid(column=0, row=1) #Set label position

month_label = tk.Label(master=window, text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(master=window, text="Day")
day_label.grid(column=0, row=3)

#Adding Entry fields for input
year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)

#Add button
calculate_button = tk.Button(master=window, text="Calculate Now")
calculate_button.grid(column=1, row=4)

class Person: #Define Person class
	def __init__(self, name, birthdate): #Pass two attributes name and birthdate
		self.name = name
		self.birthdate = birthdate

	def age(self):
		today = datetime.date.today()
		age = today.year - self.birthdate.year #Current year - birth year
		return age

christian = Person('Christian', datetime.date(1986, 10, 6)) #Create new object 'christian' with name of 'Christian' and birthdate of '10/6/1986' in a datetime format
#print(christian.name) #Print the name attribute from the `christian` object
#print(christian.birthdate) #Print the birthdate attribute from the `christian` object
#print(christian.age()) #Print age of `christian` object


window.mainloop() #builds frame