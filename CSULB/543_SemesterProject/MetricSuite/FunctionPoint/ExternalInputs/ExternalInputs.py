from tkinter import *

class ExternalInputs:

    def __init__(self, Parent):
        self.userInput = 0
        self.complexityValue = IntVar()
        self.complexityValue.set("4")
        self.parent = Parent

    def displayExternalInputs(self):
        eiLabel = Label(self.parent, text="External Inputs")
        eiLabel.grid(row=2, column=0, padx=10, pady=10)

        eiEntry = Entry(self.parent, width=10, borderwidth=5)
        eiEntry.grid(row=2, column=1, padx=10, pady=10)

        simpleRadio = Radiobutton(self.parent, text="3", variable=self.complexityValue, value=3)
        simpleRadio.grid(row=2, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(self.parent, text="4", variable=self.complexityValue, value=4)
        averageRadio.grid(row=2, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(self.parent, text="6", variable=self.complexityValue, value=6)
        complexRadio.grid(row=2, column=4, padx=10, pady=10)

        calculationLabel = Label(self.parent, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=2, column=5, padx=10, pady=10)