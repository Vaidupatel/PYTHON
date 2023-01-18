''' Operators in Python
    arithmetic operator
    assignment operator
    comparison operator
    logical operator
    identity operator
    membership operator
    bitwise operator
'''
#Arithmetic operator
print("Arithmetic operator")
print("5 + 6 is =",5+6)
print("5 - 6 is =",5-6)
print("5 * 6 is =",5*6)
print("5 / 6 is =",5/6)
print("55 // 6 is =",55//6)  #It will gives the round figure value in integer(Called as floor division operator)
print("5 ** 2 is =",5**2)  #It is exponantial operator
print("5 % 2 is =",5%2)  #It is module operator, it return reminder

#Assignment operator
print("Assignment operator")
x=5
print(x)
x+=7
# x-=7
# x*=7
# x/=7
# x%=7
print(x) #Same as x=x+7

#comparison operator
print("comparison operator")
i=8
print(i==5) # check for equal
print(i!=5) # check for not equal
print(i>5)  # check for greater
print(i<5)  # check for lesser
print(i>=5) # check for greater or equal
print(i<=5) # check for lesser or equal

#   logical operator
print("logical operator")
a=True
b=False
print(a and b)
print(a or b)

# identity operator
print("identity operator")
c=5
d=10
print(c is d)
print(c is not d)

# membership operator
print("membership operator")
list = [3,34,5,56,7,8,9,10]
print(34 in list)
print(344 in list)
print(34 not in list)
print(344 not in list)

# bitwise operator
print("bitwise operator")
print("bitwise and operator")
print(0 & 0)
print(0 & 1)
print(1 & 0)
print(1 & 1)

print("bitwise or operator")
print(0 | 0)
print(0 | 1)
print(1 | 0)
print(1 | 1)

