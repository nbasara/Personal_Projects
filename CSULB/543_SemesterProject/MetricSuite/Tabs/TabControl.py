from tkinter import *
from tkinter import ttk
from FunctionPoint.FunctionPoint import FunctionPoint

class tabControl:
    def __init__(self, Parent):
        self.tabsOpen = 0
        self.tabController = ttk.Notebook(Parent)

    def newTab(self):
        fp = FunctionPoint()
        fp.newFunctionPoint(self.tabController)
