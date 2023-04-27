class Employee:
    var = 8
    no_of_leaves = 8

    def __init__(self, anme, aslary, arole):
        self.name = anme
        self.slaray = aslary
        self.role = arole

    def printdeatils(self):
        return f"The name is {self.name}. Sallary is {self.slaray} and role is {self.role}"
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good"+string)

class player:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdeatils(self):
        return f"The name is {self.name}. Game is {self.game}"


class cool_programer(Employee,player):
    language = "c++"
    # var = 10
    def printlang(self):
        print(self.language)


vaid = Employee("vaid", 45000, "student")
nirjal = Employee("nirjal", 50000, "instructor")

prince = player("prince", ["Cricket"])
darshan = cool_programer("darshan", 50000, "cool programmer",)

# det = darshan.printdeatils()
# darshan.printlang()
# print(det)
print(darshan.var)
