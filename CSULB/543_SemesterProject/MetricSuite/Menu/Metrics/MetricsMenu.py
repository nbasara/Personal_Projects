from tkinter import *

class MetricsMenu:

    def __init__(self, parent):
        self.metricsmenu = Menu(parent.menubar, tearoff=0)
        self.submenu = Menu(parent.menubar)
        self.submenu.add_command(label="Enter FP Data", command=parent.root.addNewFunctionPoint)
        self.metricsmenu.add_cascade(label="Function Points", menu=self.submenu)