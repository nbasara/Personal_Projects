from tkinter import *

class ExternalInterfaceFiles:

    def __init__(self, Parent):
        self.userInput = 0
        self.complexityValue = IntVar()
        self.complexityValue.set("7")
        self.parent = Parent

    def displayExternalInterfaceFiles(self):
        elfLabel = Label(self.parent, text="External Interface Files")
        elfLabel.grid(row=6, column=0, padx=10, pady=10)

        elfEntry = Entry(self.parent, width=10, borderwidth=5)
        elfEntry.grid(row=6, column=1, padx=10, pady=10)

        simpleRadio = Radiobutton(self.parent, text="5", variable=self.complexityValue, value=5)
        simpleRadio.grid(row=6, column=2, padx=10, pady=10)
        
        averageRadio = Radiobutton(self.parent, text="7", variable=self.complexityValue, value=7)
        averageRadio.grid(row=6, column=3, padx=10, pady=10)

        complexRadio = Radiobutton(self.parent, text="10", variable=self.complexityValue, value=10)
        complexRadio.grid(row=6, column=4, padx=10, pady=10)

        calculationLabel = Label(self.parent, text="     ", width=10, relief="groove")
        calculationLabel.grid(row=6, column=5, padx=10, pady=10)