import tkinter as tk #GUI Library in Python named tkinter and giving it an alias of 'tk' for easier calling of methods
import webbrowser #Imports the webbrowser library


def doorbell(event): #creates function doorbell
	print("You rang the doorbell")

def open_cp(event): #Creates function open_cp
	webbrowser.open_new_tab("https://cleverprogrammer.com") #Leverages the open_new_tab function in the webbrowser library


window = tk.Tk() #Creates an object called window using the tkinter library and the Tk() method
window.geometry("300x200") #Sets the size of the window object

#Creating Labels
alabel = tk.Label(text="Banana") #Creates object alabel using the tk.Label method
alabel.grid(column=0, row=0) #Sets priority of the alabel object compared to other objects, if only object then it will still show at 0,0 (top left)

blabel = tk.Label(text="Apple")
blabel.grid(column=1, row=0)

#Creating Buttons
button = tk.Button(window, text="Doorbell") #Creates object button using the tk.Button method and displaying name "Smash"
button.grid(column=0,row=1) #Sets grid priority to place button under Banana

button2 = tk.Button(window, text="Clever Programmer") #passing the window argument makes the button a part of the frame we made
button2.grid(column=1,row=1)



button.bind("<Button-1>", doorbell) #Binds the left mouse button click to run the function doorbell when the "button" object is clicked
button2.bind("<Button-1>", open_cp) #Binds left click to button2 object to run the open_cp function

window.mainloop()