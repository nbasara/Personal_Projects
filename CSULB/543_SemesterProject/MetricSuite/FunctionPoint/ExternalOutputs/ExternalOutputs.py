from tkinter import *

class ExternalOutputs:

    def __init__(self, Parent):
        self.userInput = 0
        self.complexityValue = IntVar()
        self.complexityValue.set("5")
        self.parent = Parent

    def displayExternlOutputs(self):
        eoLabel = Label(self.parent, text="External Outputs")
        eoLabel.grid(row=3, column=0, padx=10, pady=10)

        eoEntry = Entry(self.parent, width=10, borderwidth=5)
        eoEntry.grid(row=3, column=1, padx=10, pady=10)

        simpleRadio = Radiobutton(self.parent, text="4", variable=self.complexityValue, value=4)
        simpleRadio.grid(row=3, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(self.parent, text="5", variable=self.complexityValue, value=5)
        averageRadio.grid(row=3, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(self.parent, text="7", variable=self.complexityValue, value=7)
        complexRadio.grid(row=3, column=4, padx=10, pady=10)

        calculationLabel = Label(self.parent, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=3, column=5, padx=10, pady=10)