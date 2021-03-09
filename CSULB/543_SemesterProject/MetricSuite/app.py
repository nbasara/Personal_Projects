from tkinter import *
from tkinter import ttk
from Menu.MenuBar import MenuBar
from FunctionPoint.FunctionPoint import FunctionPoint

class program:

    def __init__(self):
        self.root = Tk()
        self.tab = None
        self.projects = []

    def startProgram(self):
        self.root.geometry("1000x800")
        menubar = MenuBar(self)
        menubar.startBar()
        self.root.config(menu=menubar.menubar)

    def addNewProject(self, projectName, productName, creator, comments):
        if projectName:
            fp = FunctionPoint(
                            Project_Name=projectName,
                            Product_Name=productName,
                            Creator=creator,
                            Comments=comments
                            )
        else:
            fp = FunctionPoint(
                            Product_Name=productName,
                            Creator=creator,
                            Comments=comments
                            )
        fp.newFunctionPoint(self.tab)
        self.projects.append(fp)



    def startNewTab(self):
        self.tab = ttk.Notebook(self.root)
        return self.tab
    
    def getTab(self):
        return self.tab

def main():
    
    origin = program()
    origin.startProgram()
    origin.root.mainloop()


main()


