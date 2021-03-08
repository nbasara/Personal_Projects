from tkinter import *
from tkinter import ttk

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
    
    def externalInputs(self, parent):
        eiLabel = Label(parent, text="External Inputs")
        eiLabel.grid(row=2, column=0, padx=10, pady=10)

        eiEntry = Entry(parent, width=10, borderwidth=5)
        eiEntry.grid(row=2, column=1, padx=10, pady=10)

        complexityValue = IntVar()
        complexityValue.set("4")

        simpleRadio = Radiobutton(parent, text="3", variable=complexityValue, value=3)
        simpleRadio.grid(row=2, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(parent, text="4", variable=complexityValue, value=4)
        averageRadio.grid(row=2, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(parent, text="6", variable=complexityValue, value=6)
        complexRadio.grid(row=2, column=4, padx=10, pady=10)

        calculationLabel = Label(parent, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=2, column=5, padx=10, pady=10)
    
    def externalOutputs(self, parent):
        eoLabel = Label(parent, text="External Outputs")
        eoLabel.grid(row=3, column=0, padx=10, pady=10)

        eoEntry = Entry(parent, width=10, borderwidth=5)
        eoEntry.grid(row=3, column=1, padx=10, pady=10)

        complexityValue = IntVar()
        complexityValue.set("5")

        simpleRadio = Radiobutton(parent, text="4", variable=complexityValue, value=4)
        simpleRadio.grid(row=3, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(parent, text="5", variable=complexityValue, value=5)
        averageRadio.grid(row=3, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(parent, text="7", variable=complexityValue, value=7)
        complexRadio.grid(row=3, column=4, padx=10, pady=10)

        calculationLabel = Label(parent, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=3, column=5, padx=10, pady=10)
    
    def externalInquiries(self, parent):
        eiLabel = Label(parent, text="External Inquiries")
        eiLabel.grid(row=4, column=0, padx=10, pady=10)

        eiEntry = Entry(parent, width=10, borderwidth=5)
        eiEntry.grid(row=4, column=1, padx=10, pady=10)

        complexityValue = IntVar()
        complexityValue.set("4")

        simpleRadio = Radiobutton(parent, text="3", variable=complexityValue, value=3)
        simpleRadio.grid(row=4, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(parent, text="4", variable=complexityValue, value=4)
        averageRadio.grid(row=4, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(parent, text="6", variable=complexityValue, value=6)
        complexRadio.grid(row=4, column=4, padx=10, pady=10)

        calculationLabel = Label(parent, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=4, column=5, padx=10, pady=10)
    
    def internalLogicalFiles(self, parent):
        ilfLabel = Label(parent, text="Internal Logic Files")
        ilfLabel.grid(row=5, column=0, padx=10, pady=10)

        ilfEntry = Entry(parent, width=10, borderwidth=5)
        ilfEntry.grid(row=5, column=1, padx=10, pady=10)

        complexityValue = IntVar()
        complexityValue.set("10")

        simpleRadio = Radiobutton(parent, text="7", variable=complexityValue, value=7)
        simpleRadio.grid(row=5, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(parent, text="10", variable=complexityValue, value=10)
        averageRadio.grid(row=5, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(parent, text="15", variable=complexityValue, value=15)
        complexRadio.grid(row=5, column=4, padx=10, pady=10)

        calculationLabel = Label(parent, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=5, column=5, padx=10, pady=10)

    def externalInterfaceFiles(self, parent):
        elfLabel = Label(parent, text="External Interface Files")
        elfLabel.grid(row=6, column=0, padx=10, pady=10)

        elfEntry = Entry(parent, width=10, borderwidth=5)
        elfEntry.grid(row=6, column=1, padx=10, pady=10)

        complexityValue = IntVar()
        complexityValue.set("7")

        simpleRadio = Radiobutton(parent, text="5", variable=complexityValue, value=5)
        simpleRadio.grid(row=6, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(parent, text="7", variable=complexityValue, value=7)
        averageRadio.grid(row=6, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(parent, text="10", variable=complexityValue, value=10)
        complexRadio.grid(row=6, column=4, padx=10, pady=10)

        calculationLabel = Label(parent, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=6, column=5, padx=10, pady=10)

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
        self.externalInputs(tab)
        self.externalOutputs(tab)
        self.externalInquiries(tab)
        self.internalLogicalFiles(tab)
        self.externalInterfaceFiles(tab)
        self.totalRow(tab)
        self.computeFP(tab)
        self.valueAdjustments(tab)
        self.computeCodeSize(tab)
        self.changeLanguage(tab)
        parent.add(tab, text=self.project_name)
        parent.pack(expand=1, fill="both")
    