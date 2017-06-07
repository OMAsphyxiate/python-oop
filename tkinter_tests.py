import tkinter as tk #Import tkinter library and alias as 'tk'
import webbrowser #Import webbrowser library

def open_fb(event):
	webbrowser.open_new_tab("http://facebook.com")

def open_gmail(event):
	webbrowser.open_new_tab("http://gmail.com")

def open_so(event):
	webbrowser.open_new_tab("http://stackoverflow.com")

window_frame = tk.Tk() #Create new window
window_frame.geometry("800x600") #Set dimensions of windows to 800x600
window_frame.configure(backgroun="gray")

bookmark1 = tk.Button(window_frame, text="Facebook", background="gray")
bookmark1.grid(column=0, row=0)

bookmark2 = tk.Button(window_frame, text="GMail", background="gray")
bookmark2.grid(column=1, row=0)

bookmark3 = tk.Button(window_frame, text="Stack Overflow", background="gray")
bookmark3.grid(column=2, row=0)

bookmark1.bind("<Button-1>", open_fb)
bookmark2.bind("<Button-1>", open_gmail)
bookmark3.bind("<Button-1>", open_so)

window_frame.mainloop()