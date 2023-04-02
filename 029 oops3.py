# SELF & __INIT__
class Employee:
   no_of_leaves = 8
   def __init__(self, aname, asalary, arole):
       self.name = aname
       self.salary = asalary
       self.role = arole


    # def printdetails(self):
    #     return f"Name is {self.name}. Salary is {self.sallary}. and role is {self.role}"


vaid = Employee('vaid', 45000, 'instructor')
# nirjal = Employee()

# These are the instance but these are not the property of class
# vaid.name = 'vaid'
# vaid.sallary = 45000
# vaid.role = 'stdent'
# nirjal.name = 'nirjal'
# nirjal.sallary = 50000
# nirjal.role = 'instructor'

print(vaid.salary)
# print(nirjal.printdetails())
