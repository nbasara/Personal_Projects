class Languages:
    LanguageList = {
        "Assembler":209,
        "Ada 95":154,
        "C":148,
        "C++":59,
        "C#":58,
        "COBOL":80,
        "FORTRAN":90,
        "HTML":43,
        "Java":55,
        "JavaScript":54,
        "VBScript":38,
        "VisualBasic":50
    }
    def __init__(self):
        self.value = "None"
        self.average = 0

    def getLanguage(self):
        return self.value
    
    def getAverage(self):
        return self.average
    
    def changeLanguage(self, newValue):
        self.value =  newValue 
        self.average = self.LanguageList.get(newValue)
