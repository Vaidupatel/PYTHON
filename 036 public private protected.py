class Employee:
    no_of_leaves = 8
    var = 41
    _name = "vaidu"
    __role = "Programer"

    def __init__(self, name, sallary):
        self.name = name
        self.sallary = sallary

emp = Employee("vaidu", "Boss")

print(emp.var)
print(emp._name)
print(emp._Employee__role)
