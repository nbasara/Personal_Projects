class Languages:
    LanguageList = [
        {'name':"Assembler"},
        {'name':"Ada 95"},
        {'name':"C"},
        {'name':"C++"},
        {'name':"C#"},
        {'name':"COBOL"},
        {'name':"FORTRAN"},
        {'name':"HTML"},
        {'name':"Java"},
        {'name':"JavaScript"},
        {'name':"VBScript"},
        {'name':"VisualBasic"}
    ]
    def __init__(self):
        self.value = 'Java'

    def getLanguage(self):
        return self.value
    
    def changeLanguage(self, newValue):
        self.value =  newValue 