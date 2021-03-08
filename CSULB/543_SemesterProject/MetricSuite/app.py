from tkinter import *
from Menu.MenuBar import MenuBar
from Tabs.TabControl import tabControl

root = Tk()
#setting default value for window
root.geometry("1000x800")

menubar = MenuBar(root)
menubar.addFileMenu()
menubar.addEditMenu()
menubar.addPreferencesMenu()
menubar.addMetricsMenu()

menubar.addHelpMenu()
tab = tabControl(root)
tab.newTab()

root.config(menu=menubar.menubar)
root.mainloop()


