from tkinter import *

class InternalLogicalFiles:

    def __init__(self, Parent):
        self.userInput = 0
        self.complexityValue = IntVar()
        self.complexityValue.set("10")
        self.parent = Parent

    def displayInternalLogicalFiles(self):
        ilfLabel = Label(self.parent, text="Internal Logic Files")
        ilfLabel.grid(row=5, column=0, padx=10, pady=10)

        ilfEntry = Entry(self.parent, width=10, borderwidth=5)
        ilfEntry.grid(row=5, column=1, padx=10, pady=10)

        simpleRadio = Radiobutton(self.parent, text="7", variable=self.complexityValue, value=7)
        simpleRadio.grid(row=5, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(self.parent, text="10", variable=self.complexityValue, value=10)
        averageRadio.grid(row=5, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(self.parent, text="15", variable=self.complexityValue, value=15)
        complexRadio.grid(row=5, column=4, padx=10, pady=10)

        calculationLabel = Label(self.parent, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=5, column=5, padx=10, pady=10)