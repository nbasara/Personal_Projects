from tkinter import *

root = Tk()

#creating label widget

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="This is Nate and this is my project")

#putting onto screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()

