class Eployee:
    no_of_leaves = 8
    def __init__(self, anme, aslary, arole):
        self.name = anme
        self.slaray = aslary
        self.role = arole
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        # para = string.split("-")
        # print(para)
        # return cls(para[0], para[1], para[2])
        return cls(*string.split("-"))


class Programmer(Eployee):
    def __init__(self, anme, aslary, arole, language):
        self.name = anme
        self.slaray = aslary
        self.role = arole
        self.language = language

    def printprog(self):
        return f"The programmers name is {self.name}. salary is {self.slaray}. and roel is {self.role}. the languages are {self.language}"


vaid = Eployee("vaid", 45000, "student")
nirjal = Eployee("nirjal", 50000, "instructor")

prince = Programmer("prince", 55555, "Programmer", ["Python"])
darshan = Programmer("darshan", 45555, "Programmer", ["Python", 'cpp'])


print(darshan.printprog())
