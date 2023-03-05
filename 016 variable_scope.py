# l = 10            # Global variable
#
#
# def function(n):
#     # l=100     # Local variable
#     m = 50
#     # l=l+45      # We cant change the value of global variable in local scope
#     global l      # For changing the value of global variable in local scope we have to use globale keyword
#     l = l+45
#     print(l, m)
#     print(n, "I am in function")
#
#
# function(l)
#
# print(l)

# In the bellow example Global key word cant change the value of the
""" Because when we use the global key word control directly go out to all function
    and find the global variable and give permission to change the global variable,
    but hear x is global for all nested function of vaidu() but it's not global variable of program
"""
def vaidu():
    x = 200


    def nirjal():
        global x
        x = 300
    print("Beafor calling nirjal()",x)
    nirjal()
    print("After calling nirjal()",x)


vaidu()
