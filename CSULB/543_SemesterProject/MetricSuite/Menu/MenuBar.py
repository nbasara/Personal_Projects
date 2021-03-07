from tkinter import *
from Menu.File.FileMenu import FileMenu
from Menu.Edit.EditMenu import EditMenu
from Menu.Preference.PreferenceMenu import PreferenceMenu
from Menu.Metrics.MetricsMenu import MetricsMenu
from Menu.Help.HelpMenu import HelpMenu

class MenuBar:

    def __init__(self, parent):
        self.menubar = Menu(parent)
        self.root = parent

    def addFileMenu(self):
        fm = FileMenu(self.menubar, self.root)
        self.menubar.add_cascade(label="File", menu=fm.filemenu)
    
    def addEditMenu(self):
        em =  EditMenu(self.menubar)
        self.menubar.add_cascade(label="Edit", menu=em.editmenu)
    
    def addPreferencesMenu(self):
        pm =  PreferenceMenu(self.menubar)
        self.menubar.add_cascade(label="Preferences", menu=pm.preferencesmenu)
    
    def addMetricsMenu(self):
        pm =  MetricsMenu(self.menubar)
        self.menubar.add_cascade(label="Metrics", menu=pm.metricsmenu)
    
    def addHelpMenu(self):
        hm =  HelpMenu(self.menubar)
        self.menubar.add_cascade(label="Help", menu=hm.helpmenu)
