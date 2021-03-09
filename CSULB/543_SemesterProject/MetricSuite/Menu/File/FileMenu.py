from tkinter import *
from tkinter import ttk
from FunctionPoint.FunctionPoint import FunctionPoint

class FileMenu:

    def openNewProject(self):
        newProjectWindow = Toplevel()
        newProjectWindow.title("New Project")

        titleLabel = Label(newProjectWindow, text="CECS 543 Metrics Suite New Project")
        titleLabel.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        def start():
            if self.root.getTab() == None:
                #create new tab
                self.root.startNewTab()
                #create new FunctionPointProject
                self.root.addNewProject(
                                str(projectNameForm.get()), str(productNameForm.get()),
                                str(creatorForm.get()), str(commentForm.get("1.0", 'end-1c'))
                                )
                #close temp window
                newProjectWindow.destroy()
            else:
                self.root.addNewProject(
                                str(projectNameForm.get()), str(productNameForm.get()),
                                str(creatorForm.get()), str(commentForm.get("1.0", 'end-1c'))
                                )
                newProjectWindow.destroy()

        projectNameLabel = Label(newProjectWindow, text="Project Name:")
        projectNameLabel.grid(row=1, column=0, padx=3, pady=5)

        projectNameForm = Entry(newProjectWindow, width=30, borderwidth=3)
        projectNameForm.grid(row=1, column=1, padx=2, pady=5)

        productNameLabel = Label(newProjectWindow, text="Product Name:")
        productNameLabel.grid(row=2, column=0, padx=5, pady=5)

        productNameForm = Entry(newProjectWindow, width=30, borderwidth=3)
        productNameForm.grid(row=2, column=1, padx=2, pady=5)

        creatorLabel = Label(newProjectWindow, text="Creator:")
        creatorLabel.grid(row=3, column=0, padx=5, pady=5)

        creatorForm = Entry(newProjectWindow, width=30, borderwidth=3)
        creatorForm.grid(row=3, column=1, padx=2, pady=5)
        
        commentLabel = Label(newProjectWindow, text="Comments:")
        commentLabel.grid(row=4, column=0, padx=5, pady=5)

        commentForm = Text(newProjectWindow, width=40, height=5, borderwidth=3)
        commentForm.grid(row=5, column=0, padx=5, pady=5, columnspan=3)

        okButton = Button(newProjectWindow, text="Ok", command=start)
        okButton.grid(row=6, column=0, padx=5, pady=5)

        cancelButton = Button(newProjectWindow, text="Cancel", command=newProjectWindow.destroy)
        cancelButton.grid(row=6, column=1, padx=5, pady=5)
        

    def donothing(self):
        pass

    def __init__(self, parent):
        self.filemenu = Menu(parent.menubar, tearoff=0)
        self.root = parent.root
        self.filemenu.add_command(label="New", command=self.openNewProject)
        self.filemenu.add_command(label="Open", command=self.donothing)
        self.filemenu.add_command(label="Save", command=self.donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=parent.root.root.quit)