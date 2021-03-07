from tkinter import *

root = Tk()
#setting default value for my box
root.geometry("1000x800")

menu = LabelFrame(root, borderwidth=0)

File = Button(menu, text="File", padx=2, borderwidth=0)
Edit = Button(menu, text="Edit", padx=2, borderwidth=0)
Preferences = Button(menu, text="Preferences", padx=2, borderwidth=0)
Metrics = Button(menu, text="Metrics", padx=2, borderwidth=0)
Help = Button(menu, text="Help", padx=2, borderwidth=0)


File.grid(row=0, column=0)
Edit.grid(row=0, column=1)
Preferences.grid(row=0, column=2)
Metrics.grid(row=0, column=3)
Help.grid(row=0, column=4)

menu.grid(row=0, column=0)


root.mainloop()

