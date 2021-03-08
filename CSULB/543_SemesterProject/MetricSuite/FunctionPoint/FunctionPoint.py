from tkinter import *
from tkinter import ttk

class FunctionPoint:

    def __init__(self, Project_Name="untitled", Product_Name=None, Creator=None, Comments=None):
        self.project_name = Project_Name
        self.product_name = Product_Name
        self.creator = Creator
        self.comments = Comments

    def newFunctionPoint(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text=self.project_name)
        parent.pack(expand=1, fill="both")