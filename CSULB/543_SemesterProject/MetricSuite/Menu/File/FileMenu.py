from tkinter import *

class FileMenu:

    def donothing(self):
        pass

    def __init__(self, parent, origin):
        self.filemenu = Menu(parent, tearoff=0)
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.donothing)
        self.filemenu.add_command(label="Save", command=self.donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=origin.quit)