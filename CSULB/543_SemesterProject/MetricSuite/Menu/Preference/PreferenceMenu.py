from tkinter import *

class PreferenceMenu:

    def donothing(self):
        pass

    def __init__(self, parent):
        self.preferencesmenu = Menu(parent, tearoff=0)
        self.preferencesmenu.add_command(label="Language", command=self.donothing)