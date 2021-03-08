from tkinter import *
from tkinter import ttk
from FunctionPoint.ExternalInputs.ExternalInputs import ExternalInputs
from FunctionPoint.ExternalOutputs.ExternalOutputs import ExternalOutputs
from FunctionPoint.ExternalInquiries.ExternalInquiries import ExternalInquiries
from FunctionPoint.InternalLogicalFiles.InternalLogicalFiles import InternalLogicalFiles
from FunctionPoint.ExternalInterfaceFiles.ExternalInterfaceFiles import ExternalInterfaceFiles

class FunctionPoint:

    def __init__(self, Project_Name="untitled", Product_Name=None, Creator=None, Comments=None):
        self.project_name = Project_Name
        self.product_name = Product_Name
        self.creator = Creator
        self.comments = Comments

    def titleFrame(self, parent):
        titleLabel = Label(parent, text="Weighting Factors")
        titleLabel.config(font=("Courier", 16))
        titleLabel.grid(row=0, column=3)
    
    def complexities(self, parent):
        #simple
        simpleLabel = Label(parent, text="Simple")
        simpleLabel.config(font=("Courier", 16))   
        simpleLabel.grid(row=1, column=2)
        #Average
        averageLabel = Label(parent, text="Avergae")
        averageLabel.config(font=("Courier", 16))
        averageLabel.grid(row=1, column=3)
        #Complex
        complexLabel = Label(parent, text="Complex")
        complexLabel.config(font=("Courier", 16))
        complexLabel.grid(row=1, column=4)

    def totalRow(self, parent):
        totalLabel = Label(parent, text="Total Count")
        totalLabel.grid(row=7, column=0, padx=10, pady=10)

        outputLabel = Label(parent, text="     ", width=10, relief="groove")
        outputLabel.grid(row=7, column=5, padx=10, pady=10)

    def computeFP(self, parent):
        fpButton = Button(parent, text="Compute FP")
        fpButton.grid(row=8, column=0, padx=10, pady=10)

        fpSum = Label(parent, text="     ", width=10, relief="groove")
        fpSum.grid(row=8, column=5, padx=10, pady=10)

    def valueAdjustments(self, parent):
        vaButton = Button(parent, text="Value Adjustments")
        vaButton.grid(row=9, column=0, padx=10, pady=10)

        vaSum = Label(parent, text="     ", width=10, relief="groove")
        vaSum.grid(row=9, column=5, padx=10, pady=10)
    
    def computeCodeSize(self, parent):
        ccsButton = Button(parent, text="Compute Code Size")
        ccsButton.grid(row=10, column=0, padx=10, pady=10)

        clLabel = Label(parent, text="Current Language")
        clLabel.grid(row=10, column=2, padx=10, pady=10)

        currentLanguage = Label(parent, text="Java", width=10, relief="groove")
        currentLanguage.grid(row=10, column=3, padx=10, pady=10)  

        ccsSum = Label(parent, text="     ", width=10, relief="groove")
        ccsSum.grid(row=10, column=5, padx=10, pady=10)

    def changeLanguage(self,parent):
        changeLanguageButton = Button(parent, text="Change Language")
        changeLanguageButton.grid(row=11, column=0, padx=10, pady=10)   

    def newFunctionPoint(self, parent):
        tab = ttk.Frame(parent)
        self.titleFrame(tab)
        self.complexities(tab)
        ei = ExternalInputs(tab)
        ei.displayExternalInputs()
        eo = ExternalOutputs(tab)
        eo.displayExternlOutputs()
        ein = ExternalInquiries(tab)
        ein.displayExternalInquiries()
        ilf = InternalLogicalFiles(tab)
        ilf.displayInternalLogicalFiles()
        eif =  ExternalInterfaceFiles(tab)
        eif.displayExternalInterfaceFiles()
        self.totalRow(tab)
        self.computeFP(tab)
        self.valueAdjustments(tab)
        self.computeCodeSize(tab)
        self.changeLanguage(tab)
        parent.add(tab, text=self.project_name)
        parent.pack(expand=1, fill="both")
    