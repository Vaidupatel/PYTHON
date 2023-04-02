# STATIC METHOD
class Eployee:
    def __init__(self, anme, aslary, arole):
        self.name = anme
        self.slaray = aslary
        self.role = arole
    @staticmethod
    def printgood(string):
        print("This is good " + string)


vaid = Eployee('vaid',45000,'instructor')
# print(vaid.printgood("vaid"))
# vaid.printgood("vaid")
Eployee.printgood("vaid")
