from tkinter import *

class MetricsMenu:

    def __init__(self, parent):
        self.metricsmenu = Menu(parent.menubar, tearoff=0)
        self.submenu1 = Menu(parent.menubar)
        self.submenu1.add_command(label="Enter FP Data", command=parent.root.addNewFunctionPoint)
        self.submenu2 = Menu(parent.menubar)
        self.submenu2.add_command(label="Enter Use Case Data", command=parent.root.addNewUseCasePoint)
        self.metricsmenu.add_cascade(label="Function Points", menu=self.submenu1)
        self.metricsmenu.add_cascade(label="Use Case Points", menu=self.submenu2)