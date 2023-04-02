# CLASS METHOD AS ALTERNATE CONSTRUCTOR
class Eployee:
    no_of_leaves = 8
    def __init__(self, anme, aslary, arole):
        self.name = anme
        self.slaray = aslary
        self.role = arole


    @classmethod
    def from_dash(cls, string):
        # para = string.split("-")
        # print(para)
        # return cls(para[0], para[1], para[2])
        return cls(*string.split("-"))

prince = Eployee.from_dash("prince-47000-view")
print(prince.slaray)
print(prince.no_of_leaves)
