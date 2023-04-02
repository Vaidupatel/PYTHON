# CLASS & METHOD
class Eployee:
    no_of_leaves = 8
    def __init__(self, anme, aslary, arole):
        self.name = anme
        self.slaray = aslary
        self.role = arole
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves




vaid = Eployee('vaid',45000,'student')
nirjal = Eployee('nirjal',50000,'instructor')

vaid.change_leaves(35)

print(vaid.slaray)
print(vaid.no_of_leaves)
