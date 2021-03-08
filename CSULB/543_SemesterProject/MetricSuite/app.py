from tkinter import *
from Menu.MenuBar import MenuBar
from Tabs.TabControl import tabControl

class program:

    def __init__(self):
        self.root = Tk()

def main():
    root = Tk()
    #setting default value for window
    root.geometry("1000x800")

    menubar = MenuBar(root)
    menubar.startBar()

    menubar.addHelpMenu()
    tab = tabControl(root)
    tab.newTab()

    root.config(menu=menubar.menubar)
    root.mainloop()


main()


