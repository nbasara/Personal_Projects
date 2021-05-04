from tkinter import *
from tkinter import ttk
from Project import Project
from Menu.MenuBar import MenuBar
from FunctionPoint.FunctionPoint import FunctionPoint
from Languages.Languages import Languages
from UseCasePoint.UseCasePoint import UseCasePoint

class program:

    def __init__(self):
        self.root = Tk()
        self.tab = None
        self.project = None
        self.languages = Languages()
        self.tempFP = []
        self.tempUC = []

    def startProgram(self):
        self.root.geometry("950x1080")
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
        if len(self.tempFP) >= 1:
            self.projcet.fpWindows = self.tempFP
    
    def addNewFunctionPoint(self):
        fp = FunctionPoint(Language=self.languages.getLanguage(), 
                        Language_Average=self.languages.getAverage())
        if self.project:
            self.project.fpWindows.append(fp)
        else:
            self.tempFP.append(fp)
        fp.newFunctionPoint(self.tab)

    def loadFunctionPoint(self, fp):
        loadFP = FunctionPoint(Language=fp["language"], Language_Average=fp["languageAverage"], Value_Adjustment_Factors=fp["VAF"],
                            External_Input_Complexity=fp["eiComplexity"], External_Ouput_Complexity=fp["eoComplexity"],
                            External_Inquiries_Complexity=fp["eInqComplexity"], Internal_Logical_Files_Complexity=fp["ilfComplexity"],
                            External_Interface_Files_Complexity=fp["eifComplexity"], External_Input_Input=fp["eiInput"],
                            External_Ouput_Input=fp["eoInput"], External_Inquiries_Input=fp["eInqInput"],
                            Internal_Logical_Files_Input=fp["ilfInput"], External_Interface_Files_Input=fp["eifInput"],
                            Input_Total=fp["inputTotal"], Function_Point_Calculation=fp["functionPointCalc"])
        self.project.fpWindows.append(loadFP)
        loadFP.newFunctionPoint(self.tab)
    
    def addNewUseCasePoint(self):
        uc = UseCasePoint()
        if self.project:
            self.project.ucWindows.append(uc)
        else:
            self.tempUC.append(uc)
        uc.newUseCasePoint(self.tab)


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


