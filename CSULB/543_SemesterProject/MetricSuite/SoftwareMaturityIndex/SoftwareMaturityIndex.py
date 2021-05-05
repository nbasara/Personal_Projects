from tkinter import *
from tkinter import ttk
from tkinter import messagebox 

class SoftwareMaturityIndex:
    def __init__(self, Total=0, Entries=[]):
        self.tab = None
        self.indexFrame = None
        self.addRowActive = False
        self.total = Total
        self.smiEntry = None
        self.maEntry = None
        self.mcEntry = None
        self.mdEntry = None
        self.tmEntry = None
        self.row = 1
        self.entries = Entries


    def addRow(self):
        if not self.addRowActive:
            self.addEntries()
        else:
            return
    
    def addEntries(self):
        self.smiEntry = Entry(self.indexFrame, width=26, relief="groove")
        self.smiEntry.grid(row=self.row, column=0)

        self.maEntry = Entry(self.indexFrame, width=26, relief="groove")
        self.maEntry.grid(row=self.row, column=1)

        self.mcEntry = Entry(self.indexFrame, width=26, relief="groove")
        self.mcEntry.grid(row=self.row, column=2)

        self.mdEntry = Entry(self.indexFrame, width=26, relief="groove")
        self.mdEntry.grid(row=self.row, column=3)

        self.tmEntry = Entry(self.indexFrame, width=26, relief="groove")
        self.tmEntry.grid(row=self.row, column=4)

        self.addRowActive = True

    def computeIndex(self):
        if self.addRowActive:
            self.getEntries()
        else:
            #error
            return
    
    def getEntries(self):
        rowEntry = []
        if self.maEntry.get() == '':
            messagebox.showerror("Error", "Please Enter a number in Modules Added")
            return
        try:
            added = int(self.maEntry.get())
        except ValueError:
            messagebox.showerror("Error", "Please Enter an integer not a string in Modules Added")
            return
        if int(self.maEntry.get()) < 0:
            messagebox.showerror("Error", "Please Enter a non-negative number in Modules Added")
            return
        
        if self.mcEntry.get() == '':
            messagebox.showerror("Error", "Please Enter a number in Modules Changed")
            return
        try:
            changed = int(self.mcEntry.get())
        except ValueError:
            messagebox.showerror("Error", "Please Enter an integer not a string in Modules Changed")
            return
        if int(self.mcEntry.get()) < 0:
            messagebox.showerror("Error", "Please Enter a non-negative number in Modules Changed")
            return
        
        if self.mdEntry.get() == '':
            messagebox.showerror("Error", "Please Enter a number in Modules Deleted")
            return
        try:
            deleted = int(self.mdEntry.get())
        except ValueError:
            messagebox.showerror("Error", "Please Enter an integer not a string in Modules Deleted")
            return   
        if int(self.mdEntry.get()) < 0:
            messagebox.showerror("Error", "Please Enter a non-negative number in Modules Deleted")
            return
        
        self.total = self.total + added - deleted
        smiCalc = (self.total - (added + changed + deleted)) / self.total
        rowEntry.append(smiCalc)
        rowEntry.append(added)
        rowEntry.append(changed)
        rowEntry.append(deleted)
        rowEntry.append(self.total)
        self.entries.append(rowEntry)
        self.addRowActive = False

        smiEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(smiCalc)), state="disabled")
        smiEntry.grid(row=self.row, column=0)

        maEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(added)), state="disabled")
        maEntry.grid(row=self.row, column=1)

        mcEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(changed)), state="disabled")
        mcEntry.grid(row=self.row, column=2)

        mdEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(deleted)), state="disabled")
        mdEntry.grid(row=self.row, column=3)

        tmEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(self.total)), state="disabled")
        tmEntry.grid(row=self.row, column=4)

        self.row += 1

    def titleLabel(self):
        titleLabel = Label(self.tab, text="Software Maturity Index")
        titleLabel.config(font=("Courier", 16))
        titleLabel.grid(row=0, column=1, pady=2)
    
    def displayIndexFrame(self):
        self.indexFrame = Frame(self.tab, width=400, height=500, relief="groove", bd=4)
        self.indexFrame.grid(row=1, column=0, columnspan=4, ipady=300, padx=20, pady=20)
        
        smiLabel = Label(self.indexFrame, text="SMI", relief="groove", width=22)
        smiLabel.grid(row=0, column=0)
        maLabel = Label(self.indexFrame, text="Modules Added", relief="groove", width=22)
        maLabel.grid(row=0, column=1)
        mcLabel = Label(self.indexFrame, text="Modules Changed", relief="groove", width=22)
        mcLabel.grid(row=0, column=2)
        mcLabel = Label(self.indexFrame, text="Modules Deleted", relief="groove", width=22)
        mcLabel.grid(row=0, column=3)
        mcLabel = Label(self.indexFrame, text="Total Modules", relief="groove", width=22)
        mcLabel.grid(row=0, column=4)

    def displayButtons(self):
        addRowButton = Button(self.tab, text="Add Row", command=self.addRow)
        addRowButton.grid(row=2, column=0, padx=10, pady=10)

        computeIndexButton = Button(self.tab, text="Compute Index", command=self.computeIndex)
        computeIndexButton.grid(row=2, column=1, padx=10, pady=10)
    
    def displayEntries(self):
        for loadEntry in self.entries:
            smiEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(loadEntry[0])), state="disabled")
            smiEntry.grid(row=self.row, column=0)

            maEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(loadEntry[1])), state="disabled")
            maEntry.grid(row=self.row, column=1)

            mcEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(loadEntry[2])), state="disabled")
            mcEntry.grid(row=self.row, column=2)

            mdEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(loadEntry[3])), state="disabled")
            mdEntry.grid(row=self.row, column=3)

            tmEntry = Entry(self.indexFrame, width=26, relief="groove", textvariable=StringVar(value=str(loadEntry[4])), state="disabled")
            tmEntry.grid(row=self.row, column=4)
            
            self.row += 1

    def newSoftwareMaturityIndex(self, parent):
        self.tab = ttk.Frame(parent)
        self.titleLabel()
        self.displayIndexFrame()
        self.displayButtons()
        parent.add(self.tab, text="SMI")
        parent.pack(expand=1, fill="both")
        