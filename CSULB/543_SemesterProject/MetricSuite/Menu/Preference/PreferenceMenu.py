from tkinter import *
from Languages.Languages import Languages

class PreferenceMenu:

    def openLanguageMenu(self):
        LanguageSettings = Languages()
        LanguageSelector = Toplevel()
        language = StringVar()
        language.set(self.parent.root.languages.getLanguage())

        def done(language):
            self.parent.root.languages.changeLanguage(str(language))
            LanguageSelector.destroy()

        prompt = Label(LanguageSelector, text="Select one language", padx=10).pack()
        for name, avg in self.parent.root.languages.LanguageList.items():
            Radiobutton(LanguageSelector, text=name, variable=language, value=name).pack(anchor=W)
        doneButton = Button(LanguageSelector, text="Done", command=lambda: done(language.get())).pack()

    def __init__(self, parent):
        self.preferencesmenu = Menu(parent.menubar, tearoff=0)
        self.preferencesmenu.add_command(label="Language", command=self.openLanguageMenu)
        self.parent = parent