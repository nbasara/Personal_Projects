from tkinter import *
from tkinter import ttk
from tkinter import messagebox 

class UseCasePoint:

    def technicalComplexityFactorsWindow(self):
        Descriptions = ["Distributed System", "Performance", "End User Efficiency",
                "Complex Internal Processing", "Resusability", "Easy to Install",
                "Easy to Use", " Portable", "Easy To Change", "Concurrent",
                "Special Security Features", "Provides direct access for third parties",
                "Special User Training Facilities are Required"]
        Weights = [2, 1, 1, 1, 1, 0.5, 0.5, 2, 1, 1, 1, 1, 1]
        window = Toplevel()
        window.title("Technical Complexity Factors")

        directionLabel = Label(window, text="Assign a value from 0 to 5 for each of the following Technical Complexity Factors:")
        directionLabel.grid(row=0, column=0)
        variables = []

        def done():
            for i in range(0, len(self.TCF)):
                self.TCF[i] =  Weights[i]*variables[i].get()
            self.computeTCF()
            window.destroy()

        for i in range(0, 13):
            descriptionsLabel = Label(window, text=Descriptions[i])
            descriptionsLabel.grid(row=i+1, column=0, sticky="W")
            weightsLabel = Label(window, text=str(Weights[i]))
            weightsLabel.grid(row=i+1, column=1)
            variable = IntVar()
            variable.set(self.TCF[i]/Weights[i])
            variables.append(variable)
            dropDown = OptionMenu(window, variable, 0, 1, 2, 3, 4, 5)
            dropDown.grid(row=i+1, column=2)

        buttonFrame = Frame(window)
        doneButton = Button(buttonFrame, text="Done", command=done)
        doneButton.grid(row=0, column=0)
        cancelButton = Button(buttonFrame, text="Cancel", command=window.destroy)
        cancelButton.grid(row=0, column=1)
        buttonFrame.grid(row=len(Descriptions)+1, column=0)

    def EnvironmentalComplexityFactorsWindow(self):
        Descriptions = ["Familarity with UML", "Application Experience", "Object Oriented Experience",
                "Lead Analyst Capability", "Motivation", "Stable Requirements",
                "Part-time Workers", " Difficult Programming Language"]
        Weights = [1.5, 0.5, 1, 0.5, 1, 2, -1, 2]
        window = Toplevel()
        window.title("Environmental Complexity Factors")

        directionLabel = Label(window, text="Assign a value from 0 to 5 for each of the following Technical Complexity Factors:")
        directionLabel.grid(row=0, column=0)
        variables = []

        def done():
            for i in range(0, len(self.ECF)):
                self.ECF[i] =  Weights[i]*variables[i].get()
            self.computeECF()
            window.destroy()

        for i in range(0, 8):
            descriptionsLabel = Label(window, text=Descriptions[i])
            descriptionsLabel.grid(row=i+1, column=0, sticky="W")
            weightsLabel = Label(window, text=str(Weights[i]))
            weightsLabel.grid(row=i+1, column=1)
            variable = IntVar()
            variable.set(self.ECF[i]/Weights[i])
            variables.append(variable)
            dropDown = OptionMenu(window, variable, 0, 1, 2, 3, 4, 5)
            dropDown.grid(row=i+1, column=2)

        buttonFrame = Frame(window)
        doneButton = Button(buttonFrame, text="Done", command=done)
        doneButton.grid(row=0, column=0)
        cancelButton = Button(buttonFrame, text="Cancel", command=window.destroy)
        cancelButton.grid(row=0, column=1)
        buttonFrame.grid(row=len(Descriptions)+1, column=0)

    def doNothing(self):
        return

    def __init__(self, Technical_Complexity_Factors=[0,0,0,0,0,0,0,0,0,0,0,0,0], Environmental_Complexity_Factors=[0,0,0,0,0,0,0,0],
            UUCW_Simple_Input=0, UUCW_Average_Input=0, UUCW_Complex_Input=0,  UAW_Simple_Input=0, UAW_Average_Input=0, UAW_Complex_Input=0,
            Productivity_Factor_Input=20, LOC_Per_PM_Input=700, LOC_Per_UCP_Input=100, Use_Case_Point_Calc=0, Estimated_Hours_Calc=0,
            Estimated_LOC_Calc=0, Estimated_PM_Calc=0):
        self.tab = None
        self.TCF = Technical_Complexity_Factors
        self.TCFTotal = sum(Technical_Complexity_Factors)
        self.ECF = Environmental_Complexity_Factors
        self.ECFTotal = sum(Environmental_Complexity_Factors)
        self.uucwSimpleInput = UUCW_Simple_Input
        self.uucwSimpleEntry = None
        self.uucwAverageInput = UUCW_Average_Input
        self.uucwAverageEntry = None
        self.uucwComplexInput = UUCW_Complex_Input
        self.uucwComplexEntry = None
        self.uucwTotal = self.uucwSimpleInput*5 + self. uucwAverageInput*10 + self.uucwComplexInput*15
        self.uawSimpleInput = UAW_Simple_Input
        self.uawSimpleEntry = None
        self.uawAverageInput = UAW_Average_Input
        self.uawAverageEntry = None
        self.uawComplexInput = UAW_Complex_Input
        self.uawComplexEntry = None
        self.uawTotal = self.uawSimpleInput*5 + self. uawAverageInput*10 + self.uawComplexInput*15
        self.uucpTotal = self.uawTotal + self.uucwTotal
        self.productivityFactorInput = Productivity_Factor_Input
        self.productivityFactorEntry = None
        self.locPerPMInput = LOC_Per_PM_Input
        self.locPerPMEntry = None
        self.locPerUCPInput = LOC_Per_UCP_Input
        self.locPerUCPEntry = None
        self.useCasePointCalc = Use_Case_Point_Calc
        self.estimatedHoursCalc = Estimated_Hours_Calc
        self.estimatedLOCCalc = Estimated_LOC_Calc
        self.estimatedPMCalc = Estimated_PM_Calc

    def titleFrame(self):
        titleLabel = titleLabel = Label(self.tab, text="Use Case Points")
        titleLabel.config(font=("Courier", 16))
        titleLabel.grid(row=0, column=2)

    def technicalComplexityFactors(self):
        tcfButton = Button(self.tab, text="Technical Complexity Factors", command=self.technicalComplexityFactorsWindow)
        tcfButton.grid(row=1, column=0, padx=10, pady=10)

        tcfSum = Label(self.tab, text=str(self.TCFTotal), width=10, relief="groove")
        tcfSum.grid(row=1, column=3, padx=10, pady=10)
    
    def environmentalComplexityFactors(self):
        ecfButton = Button(self.tab, text="Environmental Complexity Factors", command=self.EnvironmentalComplexityFactorsWindow)
        ecfButton.grid(row=2, column=0, padx=10, pady=10)

        ecfSum = Label(self.tab, text=str(self.ECFTotal), width=10, relief="groove")
        ecfSum.grid(row=2, column=3, padx=10, pady=10)

    def displayUUCW(self):
        #display division label
        divisionLabel = Label(self.tab, text="Unadjusted Use Case Weight")
        divisionLabel.config(font=("Courier", 12))
        divisionLabel.grid(row=3, column=2, padx=10, pady=10)
        #display column identifier
        useCaseTypeLabel = Label(self.tab, text="Use Case Type")
        useCaseTypeLabel.config(font=("Courier", 12))
        useCaseTypeLabel.grid(row=4, column=0, padx=10, pady=10)

        weightLabel = Label(self.tab, text="Weight")
        weightLabel.config(font=("Courier", 12))
        weightLabel.grid(row=4, column=1, padx=10, pady=10)

        nUseCaseLabel = Label(self.tab, text="Number of Use Cases")
        nUseCaseLabel.config(font=("Courier", 12))
        nUseCaseLabel.grid(row=4, column=2, padx=10, pady=10)

        resultLabel = Label(self.tab, text="Result")
        resultLabel.config(font=("Courier", 12))
        resultLabel.grid(row=4, column=3, padx=10, pady=10)
    
    def uucwSimple(self):
        simpleLabel = Label(self.tab, text="Simple")
        simpleLabel.grid(row=5, column=0, padx=10, pady=10)

        simpleWeightLabel = Label(self.tab, text="5")
        simpleWeightLabel.grid(row=5, column=1, padx=10, pady=10)

        self.uucwSimpleEntry = Entry(self.tab, textvariable=StringVar(value=str(self.uucwSimpleInput)), width=10, borderwidth=5)
        self.uucwSimpleEntry.grid(row=5, column=2, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uucwSimpleInput) * 5)), width=10, relief="groove")
        calculationLabel.grid(row=5, column=3, padx=10, pady=10)

    def uucwAverage(self):
        averageLabel = Label(self.tab, text="Average")
        averageLabel.grid(row=6, column=0, padx=10, pady=10)

        averageWeightLabel = Label(self.tab, text="10")
        averageWeightLabel.grid(row=6, column=1, padx=10, pady=10)

        self.uucwAverageEntry = Entry(self.tab, textvariable=StringVar(value=str(self.uucwAverageInput)), width=10, borderwidth=5)
        self.uucwAverageEntry.grid(row=6, column=2, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uucwAverageInput) * 10)), width=10, relief="groove")
        calculationLabel.grid(row=6, column=3, padx=10, pady=10)

    def uucwComplex(self):
        complexLabel = Label(self.tab, text="Complex")
        complexLabel.grid(row=7, column=0, padx=10, pady=10)

        complexWeightLabel = Label(self.tab, text="15")
        complexWeightLabel.grid(row=7, column=1, padx=10, pady=10)

        self.uucwComplexEntry = Entry(self.tab, textvariable=StringVar(value=str(self.uucwComplexInput)), width=10, borderwidth=5)
        self.uucwComplexEntry.grid(row=7, column=2, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uucwComplexInput) * 15)), width=10, relief="groove")
        calculationLabel.grid(row=7, column=3, padx=10, pady=10)

    def displayUAW(self):
        #display division label
        divisionLabel = Label(self.tab, text="Unadjusted Actor Weight")
        divisionLabel.config(font=("Courier", 12))
        divisionLabel.grid(row=8, column=2, padx=10, pady=10)
        #display column identifier
        useCaseTypeLabel = Label(self.tab, text="Use Case Type")
        useCaseTypeLabel.config(font=("Courier", 12))
        useCaseTypeLabel.grid(row=9, column=0, padx=10, pady=10)

        weightLabel = Label(self.tab, text="Weight")
        weightLabel.config(font=("Courier", 12))
        weightLabel.grid(row=9, column=1, padx=10, pady=10)

        nUseCaseLabel = Label(self.tab, text="Number of Use Cases")
        nUseCaseLabel.config(font=("Courier", 12))
        nUseCaseLabel.grid(row=9, column=2, padx=10, pady=10)

        resultLabel = Label(self.tab, text="Result")
        resultLabel.config(font=("Courier", 12))
        resultLabel.grid(row=9, column=3, padx=10, pady=10)

    def uawSimple(self):
        simpleLabel = Label(self.tab, text="Simple")
        simpleLabel.grid(row=10, column=0, padx=10, pady=10)

        simpleWeightLabel = Label(self.tab, text="5")
        simpleWeightLabel.grid(row=10, column=1, padx=10, pady=10)

        self.uawSimpleEntry = Entry(self.tab, textvariable=StringVar(value=str(self.uawSimpleInput)), width=10, borderwidth=5)
        self.uawSimpleEntry.grid(row=10, column=2, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uawSimpleInput) * 5)), width=10, relief="groove")
        calculationLabel.grid(row=10, column=3, padx=10, pady=10)

    def uawAverage(self):
        averageLabel = Label(self.tab, text="Average")
        averageLabel.grid(row=11, column=0, padx=10, pady=10)

        averageWeightLabel = Label(self.tab, text="10")
        averageWeightLabel.grid(row=11, column=1, padx=10, pady=10)

        self.uawAverageEntry = Entry(self.tab, textvariable=StringVar(value=str(self.uawAverageInput)), width=10, borderwidth=5)
        self.uawAverageEntry.grid(row=11, column=2, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uawAverageInput) * 10)), width=10, relief="groove")
        calculationLabel.grid(row=11, column=3, padx=10, pady=10)

    def uawComplex(self):
        complexLabel = Label(self.tab, text="Complex")
        complexLabel.grid(row=12, column=0, padx=10, pady=10)

        complexWeightLabel = Label(self.tab, text="15")
        complexWeightLabel.grid(row=12, column=1, padx=10, pady=10)

        self.uawComplexEntry = Entry(self.tab, textvariable=StringVar(value=str(self.uawComplexInput)), width=10, borderwidth=5)
        self.uawComplexEntry.grid(row=12, column=2, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uawComplexInput) * 15)), width=10, relief="groove")
        calculationLabel.grid(row=12, column=3, padx=10, pady=10)

    def unadjustedUseCasePoint(self):
        uucpLabel = Label(self.tab, text="Unadjusted Use Case Point")
        uucpLabel.config(font=("Courier", 12))
        uucpLabel.grid(row=13, column=2, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uucpTotal))), width=10, relief="groove")
        calculationLabel.grid(row=13, column=3, padx=10, pady=10)

    def productivity(self):
        pfLabel = Label(self.tab, text="Productivity Factor")
        pfLabel.config(font=("Courier", 12))
        pfLabel.grid(row=14, column=0, padx=10, pady=10)

        self.productivityFactorEntry = Entry(self.tab, textvariable=StringVar(value=str(self.productivityFactorInput)), width=10, borderwidth=5)    
        self.productivityFactorEntry.grid(row=14, column=1, padx=10, pady=10)

    def locPerPM(self):
        locPerPMLabel = Label(self.tab, text="LOC per Person Month")
        locPerPMLabel.config(font=("Courier", 12))
        locPerPMLabel.grid(row=15, column=0, padx=10, pady=10)

        self.locPerPMEntry = Entry(self.tab, textvariable=StringVar(value=str(self.locPerPMInput)), width=10, borderwidth=5)    
        self.locPerPMEntry.grid(row=15, column=1, padx=10, pady=10)

    def locPerUCP(self):
        locPerUCPLabel = Label(self.tab, text="LOC per Use Case Point")
        locPerUCPLabel.config(font=("Courier", 12))
        locPerUCPLabel.grid(row=16, column=0, padx=10, pady=10)

        self.locPerUCPEntry = Entry(self.tab, textvariable=StringVar(value=str(self.locPerUCPInput)), width=10, borderwidth=5)    
        self.locPerUCPEntry.grid(row=16, column=1, padx=10, pady=10)

    def totals(self):
        def calculation():
            self.computeUUCP()
            self.useCasePointCalc = self.uucpTotal * self.ECFTotal * self.TCFTotal
            ucpTotal = Label(self.tab, text=f"{self.useCasePointCalc:,.2f}", width=15, relief="groove")
            ucpTotal.grid(row=17, column=3, padx=10, pady=10)

            self.estimatedHoursCalc = self.useCasePointCalc * int(self.productivityFactorEntry.get())
            estimatedHoursTotal = Label(self.tab, text=f"{self.estimatedHoursCalc:,.2f}", width=15, relief="groove")
            estimatedHoursTotal.grid(row=18, column=3, padx=10, pady=10)

            self.estimatedLOCCalc = self.useCasePointCalc * int( self.locPerUCPEntry.get())
            estimatedLOCTotal = Label(self.tab, text=f"{self.estimatedLOCCalc:,.2f}", width=15, relief="groove")
            estimatedLOCTotal.grid(row=19, column=3, padx=10, pady=10)

            self.estimatedPMCalc = self.estimatedLOCCalc / int(self.locPerPMEntry.get())
            estimatedPMTotal = Label(self.tab, text=f"{self.estimatedPMCalc:,.2f}", width=15, relief="groove")
            estimatedPMTotal.grid(row=20, column=3, padx=10, pady=10)


        ucpButton = Button(self.tab, text="Compute UCP", command=calculation)
        ucpButton.grid(row=17, column=0, padx=10, pady=10)

        ucpLabel = Label(self.tab, text="Use Case Point Total", width=15, relief="groove")
        ucpLabel.grid(row=17, column=2, padx=10, pady=10)

        ucpTotal = Label(self.tab, text=f"{self.useCasePointCalc:,.2f}", width=15, relief="groove")
        ucpTotal.grid(row=17, column=3, padx=10, pady=10)

        estimatedHoursLabel = Label(self.tab, text="Estimated Hours", width=15, relief="groove")
        estimatedHoursLabel.grid(row=18, column=2, padx=10, pady=10)

        estimatedHoursTotal = Label(self.tab, text=f"{self.estimatedHoursCalc:,.2f}", width=15, relief="groove")
        estimatedHoursTotal.grid(row=18, column=3, padx=10, pady=10)

        estimatedLOCLabel = Label(self.tab, text="Estimated LOC", width=15, relief="groove")
        estimatedLOCLabel.grid(row=19, column=2, padx=10, pady=10)

        estimatedLOCTotal = Label(self.tab, text=f"{self.estimatedLOCCalc:,.2f}", width=15, relief="groove")
        estimatedLOCTotal.grid(row=19, column=3, padx=10, pady=10)

        estimatedPMLabel = Label(self.tab, text="Estimated PM", width=15, relief="groove")
        estimatedPMLabel.grid(row=20, column=2, padx=10, pady=10)

        estimatedPMTotal = Label(self.tab, text=f"{self.estimatedPMCalc:,.2f}", width=15, relief="groove")
        estimatedPMTotal.grid(row=20, column=3, padx=10, pady=10)

    def computeTCF(self):
        self.TCFTotal = round(0.6 + (0.1*sum(self.TCF)), 2)
        tcfSum = Label(self.tab, text=str(self.TCFTotal), width=10, relief="groove")
        tcfSum.grid(row=1, column=3, padx=10, pady=10)

    def computeECF(self):
        self.ECFTotal = round(1.4 + (-0.03*sum(self.ECF)), 2)
        ecfSum = Label(self.tab, text=str(self.ECFTotal), width=10, relief="groove")
        ecfSum.grid(row=2, column=3, padx=10, pady=10)

    def computeUUCW(self):
        calculationLabel = Label(self.tab, text=str((int(self.uucwSimpleEntry.get()) * 5)), width=10, relief="groove")
        calculationLabel.grid(row=5, column=3, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uucwAverageEntry.get()) * 10)), width=10, relief="groove")
        calculationLabel.grid(row=6, column=3, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uucwComplexEntry.get()) * 15)), width=10, relief="groove")
        calculationLabel.grid(row=7, column=3, padx=10, pady=10)

        self.uucwTotal = int(self.uucwSimpleEntry.get())*5 + int(self.uucwAverageEntry.get())*10 + int(self.uucwComplexEntry.get())*15
    
    def computeUAW(self):
        calculationLabel = Label(self.tab, text=str((int(self.uawSimpleEntry.get()) * 5)), width=10, relief="groove")
        calculationLabel.grid(row=10, column=3, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uawAverageEntry.get()) * 10)), width=10, relief="groove")
        calculationLabel.grid(row=11, column=3, padx=10, pady=10)

        calculationLabel = Label(self.tab, text=str((int(self.uawComplexEntry.get()) * 15)), width=10, relief="groove")
        calculationLabel.grid(row=12, column=3, padx=10, pady=10)

        self.uawTotal = int(self.uawSimpleEntry.get())*5 + int(self.uawAverageEntry.get())*10 + int(self.uawComplexEntry.get())*15

    def computeUUCP(self):
        self.computeUUCW()
        self.computeUAW()
        self.uucpTotal = self.uucwTotal + self.uawTotal
        calculationLabel = Label(self.tab, text=str((int(self.uucpTotal))), width=10, relief="groove")
        calculationLabel.grid(row=13, column=3, padx=10, pady=10)

    def newUseCasePoint(self, parent):
        self.tab = ttk.Frame(parent)
        self.titleFrame()
        self.technicalComplexityFactors()
        self.environmentalComplexityFactors()
        self.displayUUCW()
        self.uucwSimple()
        self.uucwAverage()
        self.uucwComplex()
        self.displayUAW()
        self.uawSimple()
        self.uawAverage()
        self.uawComplex()
        self.unadjustedUseCasePoint()
        self.productivity()
        self.locPerPM()
        self.locPerUCP()
        self.totals()
        parent.add(self.tab, text="Use Case Point")
        parent.pack(expand=1, fill="both")
