class Employee:
    no_of_leaves = 8
    pass


vaid = Employee()
nirjal = Employee()

# These are the instance but these are not the property of class
vaid.name = 'vaid'
vaid.sallary = 45000
vaid.role = 'stdent'
nirjal.name = 'nirjal'
nirjal.sallary = 50000
nirjal.role = 'instructor'

# We can access property of class using class or class instance
print(vaid.no_of_leaves)
print(Employee.no_of_leaves)
print(vaid.__dict__)

# But, if we want to change the property of class thane we have use class
Employee.no_of_leaves = 10
vaid.no_of_leaves = 5
print(vaid.__dict__)
print(Employee.no_of_leaves)
print(Employee.__dict__)
