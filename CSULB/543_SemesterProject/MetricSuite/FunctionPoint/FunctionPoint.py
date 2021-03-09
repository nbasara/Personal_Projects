from tkinter import *
from tkinter import ttk
from Languages.Languages import Languages

class FunctionPoint:

    LanguageSetting = Languages()

    def valueAdjustmentsWindow(self):

        valueAdjustmentFactors = [
            "Does the system require reliable back and recovery processes?",
            "Are specialize data communications required to transfer information to or from the application?",
            "Are there distributed processing functions?",
            "Is performance critical",
            "Will the system run in an existing, heavily utilized operational environment?",
            "Will the system require online data entry?",
            "Does the online data entry require the input transaction to be built over multiple screens or operations?",
            "Are the internal logical files updated online?",
            "Are the input, ouput, files or inquires complex?",
            "Is the code designed to be reusable?",
            "Are conversion and installation included in the deign?",
            "Is the system designed or multiple installations in different organizations?",
            "Is the application designed to facilitate change and for ease of use by the user?"
        ]

        window = Toplevel()
        window.title("Value Adjustment Factors")

        directionLabel = Label(window, text="Assign a value from 0 to 5 for each of the following Value Adjustment Factors:")
        directionLabel.grid(row=0, column=0)
        variables = []

        def done():
            for i in range(0, len(self.VAF)):
                self.VAF[i] = variables[i].get()
            self.computeVAF()
            window.destroy()

        for i in range(0, len(valueAdjustmentFactors)):
            label = Label(window, text=valueAdjustmentFactors[i])
            label.grid(row=i+1, column=0, sticky="W")
            variable = IntVar()
            variable.set(self.VAF[i])
            variables.append(variable)
            dropDown = OptionMenu(window, variable, 0, 1, 2, 3, 4, 5)
            dropDown.grid(row=i+1, column=1)

        buttonFrame = Frame(window)
        doneButton = Button(buttonFrame, text="Done", command=done)
        doneButton.grid(row=0, column=0)
        cancelButton = Button(buttonFrame, text="Cancel", command=window.destroy)
        cancelButton.grid(row=0, column=1)
        buttonFrame.grid(row=len(valueAdjustmentFactors)+1, column=0)




    def __init__(self, Project_Name="untitled", Product_Name=None, Creator=None, Comments=None, External_Input_Complexity=4,
             External_Ouput_Complexity=5, External_Inquiries_Complexity=4, Internal_Logical_Files_Complexity=10, 
             External_Interface_Files_Complexity=7, External_Input_Input=0, External_Ouput_Input=0, External_Inquiries_Input=0,
             Internal_Logical_Files_Input=0, External_Interface_Files_Input=0, Value_Adjustment_Factors=[0,0,0,0,0,0,0,0,0,0,0,0,0],
             Language=LanguageSetting.getLanguage(), Input_Total=0, Function_Point_Calculation=0):
        self.tab = None
        self.project_name = Project_Name
        self.product_name = Product_Name
        self.creator = Creator
        self.comments = Comments
        self.eiComplexity = IntVar()
        self.eiComplexity.set(External_Input_Complexity)
        self.eoComplexity = IntVar()
        self.eoComplexity.set(External_Ouput_Complexity)
        self.eInqComplexity = IntVar()
        self.eInqComplexity.set(External_Inquiries_Complexity)
        self.ilfComplexity = IntVar()
        self.ilfComplexity.set(Internal_Logical_Files_Complexity)
        self.eifComplexity = IntVar()
        self.eifComplexity.set(External_Interface_Files_Complexity)
        self.eiInput = External_Input_Input
        self.eoInput = External_Ouput_Input
        self.eInqInput = External_Inquiries_Input
        self.ilfInput = Internal_Logical_Files_Input
        self.eifInput = External_Interface_Files_Input
        self.VAF = Value_Adjustment_Factors
        self.language = Language
        self.inputTotal = Input_Total
        self.functionPointCalc = Function_Point_Calculation
        self.VAFtotal = 0

    def titleFrame(self):
        titleLabel = Label(self.tab, text="Weighting Factors")
        titleLabel.config(font=("Courier", 16))
        titleLabel.grid(row=0, column=3)
    
    def complexities(self):
        #simple
        simpleLabel = Label(self.tab, text="Simple")
        simpleLabel.config(font=("Courier", 16))   
        simpleLabel.grid(row=1, column=2)
        #Average
        averageLabel = Label(self.tab, text="Avergae")
        averageLabel.config(font=("Courier", 16))
        averageLabel.grid(row=1, column=3)
        #Complex
        complexLabel = Label(self.tab, text="Complex")
        complexLabel.config(font=("Courier", 16))
        complexLabel.grid(row=1, column=4)

    def displayExternalInputs(self):
        eiLabel = Label(self.tab, text="External Inputs")
        eiLabel.grid(row=2, column=0, padx=10, pady=10)

        eiEntry = Entry(self.tab, width=10, borderwidth=5)
        eiEntry.grid(row=2, column=1, padx=10, pady=10)

        simpleRadio = Radiobutton(self.tab, text="3", variable=self.eiComplexity, value=3)
        simpleRadio.grid(row=2, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(self.tab, text="4", variable=self.eiComplexity, value=4)
        averageRadio.grid(row=2, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(self.tab, text="6", variable=self.eiComplexity, value=6)
        complexRadio.grid(row=2, column=4, padx=10, pady=10)

        calculationLabel = Label(self.tab, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=2, column=5, padx=10, pady=10)
    
    def displayExternlOutputs(self):
        eoLabel = Label(self.tab, text="External Outputs")
        eoLabel.grid(row=3, column=0, padx=10, pady=10)

        eoEntry = Entry(self.tab, width=10, borderwidth=5)
        eoEntry.grid(row=3, column=1, padx=10, pady=10)

        simpleRadio = Radiobutton(self.tab, text="4", variable=self.eoComplexity, value=4)
        simpleRadio.grid(row=3, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(self.tab, text="5", variable=self.eoComplexity, value=5)
        averageRadio.grid(row=3, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(self.tab, text="7", variable=self.eoComplexity, value=7)
        complexRadio.grid(row=3, column=4, padx=10, pady=10)

        calculationLabel = Label(self.tab, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=3, column=5, padx=10, pady=10)

    def displayExternalInquiries(self):
        eiLabel = Label(self.tab, text="External Inquiries")
        eiLabel.grid(row=4, column=0, padx=10, pady=10)

        eiEntry = Entry(self.tab, width=10, borderwidth=5)
        eiEntry.grid(row=4, column=1, padx=10, pady=10)

        simpleRadio = Radiobutton(self.tab, text="3", variable=self.eInqComplexity, value=3)
        simpleRadio.grid(row=4, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(self.tab, text="4", variable=self.eInqComplexity, value=4)
        averageRadio.grid(row=4, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(self.tab, text="6", variable=self.eInqComplexity, value=6)
        complexRadio.grid(row=4, column=4, padx=10, pady=10)

        calculationLabel = Label(self.tab, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=4, column=5, padx=10, pady=10)

    def displayInternalLogicalFiles(self):
        ilfLabel = Label(self.tab, text="Internal Logic Files")
        ilfLabel.grid(row=5, column=0, padx=10, pady=10)

        ilfEntry = Entry(self.tab, width=10, borderwidth=5)
        ilfEntry.grid(row=5, column=1, padx=10, pady=10)

        simpleRadio = Radiobutton(self.tab, text="7", variable=self.ilfComplexity, value=7)
        simpleRadio.grid(row=5, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(self.tab, text="10", variable=self.ilfComplexity, value=10)
        averageRadio.grid(row=5, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(self.tab, text="15", variable=self.ilfComplexity, value=15)
        complexRadio.grid(row=5, column=4, padx=10, pady=10)

        calculationLabel = Label(self.tab, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=5, column=5, padx=10, pady=10)

    def displayExternalInterfaceFiles(self):
        elfLabel = Label(self.tab, text="External Interface Files")
        elfLabel.grid(row=6, column=0, padx=10, pady=10)

        elfEntry = Entry(self.tab, width=10, borderwidth=5)
        elfEntry.grid(row=6, column=1, padx=10, pady=10)

        simpleRadio = Radiobutton(self.tab, text="5", variable=self.eifComplexity, value=5)
        simpleRadio.grid(row=6, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(self.tab, text="7", variable=self.eifComplexity, value=7)
        averageRadio.grid(row=6, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(self.tab, text="10", variable=self.eifComplexity, value=10)
        complexRadio.grid(row=6, column=4, padx=10, pady=10)

        calculationLabel = Label(self.tab, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=6, column=5, padx=10, pady=10)

    def totalRow(self):
        totalLabel = Label(self.tab, text="Total Count")
        totalLabel.grid(row=7, column=0, padx=10, pady=10)

        outputLabel = Label(self.tab, text="     ", width=10, relief="groove")
        outputLabel.grid(row=7, column=5, padx=10, pady=10)

    def computeFP(self):
        fpButton = Button(self.tab, text="Compute FP")
        fpButton.grid(row=8, column=0, padx=10, pady=10)

        fpSum = Label(self.tab, text="     ", width=10, relief="groove")
        fpSum.grid(row=8, column=5, padx=10, pady=10)

    def valueAdjustments(self):
        vaButton = Button(self.tab, text="Value Adjustments", command=self.valueAdjustmentsWindow)
        vaButton.grid(row=9, column=0, padx=10, pady=10)

        vaSum = Label(self.tab, text=str(self.VAFtotal), width=10, relief="groove")
        vaSum.grid(row=9, column=5, padx=10, pady=10)

    def computeVAF(self):
        total = 0
        for n in self.VAF:
            total += n
        self.VAFtotal = total
        vaSum = Label(self.tab, text=str(self.VAFtotal), width=10, relief="groove")
        vaSum.grid(row=9, column=5, padx=10, pady=10)
    
    def computeCodeSize(self):
        ccsButton = Button(self.tab, text="Compute Code Size")
        ccsButton.grid(row=10, column=0, padx=10, pady=10)

        clLabel = Label(self.tab, text="Current Language")
        clLabel.grid(row=10, column=2, padx=10, pady=10)

        currentLanguage = Label(self.tab, text="Java", width=10, relief="groove")
        currentLanguage.grid(row=10, column=3, padx=10, pady=10)  

        ccsSum = Label(self.tab, text="     ", width=10, relief="groove")
        ccsSum.grid(row=10, column=5, padx=10, pady=10)

    def changeLanguage(self):
        changeLanguageButton = Button(self.tab, text="Change Language")
        changeLanguageButton.grid(row=11, column=0, padx=10, pady=10)   

    def newFunctionPoint(self, parent):
        self.tab = ttk.Frame(parent)
        self.titleFrame()
        self.complexities()
        self.displayExternalInputs()
        self.displayExternlOutputs()
        self.displayExternalInquiries()
        self.displayInternalLogicalFiles()
        self.displayExternalInterfaceFiles()
        self.totalRow()
        self.computeFP()
        self.valueAdjustments()
        self.computeCodeSize()
        self.changeLanguage()
        parent.add(self.tab, text=self.project_name)
        parent.pack(expand=1, fill="both")
    