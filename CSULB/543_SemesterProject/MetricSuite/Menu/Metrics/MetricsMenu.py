from tkinter import *

class MetricsMenu:

    def donothing(self):
        pass

    def __init__(self, parent):
        self.metricsmenu = Menu(parent, tearoff=0)
        self.metricsmenu.add_command(label="Function Points", command=self.donothing)