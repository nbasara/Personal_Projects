from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from Project import Project
from Menu.MenuBar import MenuBar
from FunctionPoint.FunctionPoint import FunctionPoint
from Languages.Languages import Languages
from UseCasePoint.UseCasePoint import UseCasePoint
from SoftwareMaturityIndex.SoftwareMaturityIndex import SoftwareMaturityIndex

class program:

    def __init__(self):
        self.root = Tk()
        self.tab = None
        self.project = None
        self.languages = Languages()
        self.tempSMIPanel = None
        self.menubar = None

    def startProgram(self):
        self.root.geometry("950x1080")
        self.root.title("CECS 543 Metrics Suite")
        self.menubar = MenuBar(self)
        self.menubar.startBar()
        self.root.config(menu=self.menubar.menubar)
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
            messagebox.showerror("Error", "Please open a project before opening a metric")
            return
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
            messagebox.showerror("Error", "Please open a project before opening a metric")
            return
        uc.newUseCasePoint(self.tab)

    def loadUseCasePoint(self, ucp):
        loadUCP = UseCasePoint(Technical_Complexity_Factors=ucp["TCF"], Environmental_Complexity_Factors=ucp["ECF"],
            UUCW_Simple_Input=ucp["uucwSimpleInput"], UUCW_Average_Input=ucp[ "uucwAverageInput"], 
            UUCW_Complex_Input=ucp["uucwComplexInput"],  UAW_Simple_Input=ucp["uawSimpleInput"], 
            UAW_Average_Input=ucp["uawAverageInput"], UAW_Complex_Input=ucp["uawComplexInput"],
            Productivity_Factor_Input=ucp["productivityFactorEntry"], LOC_Per_PM_Input=ucp["locPerPMEntry"], 
            LOC_Per_UCP_Input=ucp["locPerUCPEntry"], Use_Case_Point_Calc=ucp["useCasePointCalc"], Estimated_Hours_Calc=ucp["estimatedHoursCalc"],
            Estimated_LOC_Calc=ucp["estimatedLOCCalc"], Estimated_PM_Calc=ucp["estimatedPMCalc"])
        self.project.ucWindows.append(loadUCP)
        loadUCP.newUseCasePoint(self.tab)
    
    def addNewSoftwareMaturityIndex(self):
        smi = SoftwareMaturityIndex()
        if self.project:
            if self.project.smiPanel == None:
                self.project.smiPanel = smi
            else:
                messagebox.showerror("Error", "There is already a Software Maturity Panel for this Project")
                return
        else:
            messagebox.showerror("Error", "Please open a project before opening a metric")
            return
        smi.newSoftwareMaturityIndex(self.tab)
    
    def loadSoftwareMaturityIndex(self, smi):
        if smi[len(smi)-1][4] != 0:
            loadSMI = SoftwareMaturityIndex(Total=smi[len(smi)-1][4], Entries=smi)
        else:
            loadSMI = SoftwareMaturityIndex(Entries=smi)
        self.project.smiPanel = loadSMI
        loadSMI.newSoftwareMaturityIndex(self.tab)
        loadSMI.displayEntries()
        

    def startNewTab(self):
        self.tab = ttk.Notebook(self.root)
        return self.tab
    
    def getTab(self):
        return self.tab
    
    def saveChanges(self):
        response =  messagebox.askyesnocancel("Save/DiscardChanges", "Do you wish to save changes?")
        if response:
            self.menubar.fm.projectSave()
            self.root.destroy()
        elif response == None:
            return
        else:
            self.root.destroy()

            

def main():
    
    origin = program()
    origin.startProgram()
    origin.root.protocol("WM_DELETE_WINDOW", origin.saveChanges)
    origin.root.mainloop()


main()


