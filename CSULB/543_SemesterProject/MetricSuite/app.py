from tkinter import *
from tkinter import ttk
from Project import Project
from Menu.MenuBar import MenuBar
from FunctionPoint.FunctionPoint import FunctionPoint
from Languages.Languages import Languages

class program:

    def __init__(self):
        self.root = Tk()
        self.tab = None
        self.project = None
        self.languages = Languages()
        self.tempFP = []

    def startProgram(self):
        self.root.geometry("1000x800")
        self.root.title("CECS 543 Metrics Suite")
        menubar = MenuBar(self)
        menubar.startBar()
        self.root.config(menu=menubar.menubar)
        self.startNewTab()

    def addNewProject(self, projectName, productName, creator, comments):
        if projectName:
            self.project = Project(
                            Project_Name=projectName,
                            Product_Name=productName,
                            Creator=creator,
                            Comments=comments
                            )
            self.root.title("CECS 543 Metrics Suite - " + projectName)
        else:
            self.project = Project(
                            Project_Name="untitled",
                            Product_Name=productName,
                            Creator=creator,
                            Comments=comments
                            )
            self.root.title("CECS 543 Metrics Suite - " + "untitled")
    
    def addNewFunctionPoint(self):
        fp = FunctionPoint(Language=self.languages.getLanguage(), 
                        Language_Average=self.languages.getAverage())
        if self.project:
            self.project.fpWindows.append(fp)
        else:
            self.tempFP.append(fp)
        fp.newFunctionPoint(self.tab)


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


