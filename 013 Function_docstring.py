a=9
b=8
c=sum((a,b))    #Built in function
print(c)

def function1(a,b):
    print("This is function1",a+b)
function1(6,7) #This statement is exicute functon1 and what ever in functoin1 will exicute

def function2(a,b):
    #In functon, First line of function written as a multie comment is called Docstring
    """This is a function which one is calculate the average of 2 numbers """
    average=(a+b)/2
    return average  #If we cant return vale, than we can not assign any variable to function
v=function2(6,4)
print(v)    #It will return none, because thare is no return value
print(function2.__doc__)
