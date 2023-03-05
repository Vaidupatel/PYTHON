# n!=n* n-1* n-2* n-3*........1
# n!=n* (n-1)!
# Below example is iterative method

# def iterative_factorial(n):
#     fact = 1
#     for i in range(n):
#         fact = fact * (i+1)
#     return fact
#     pass
#
#
# num = int(input("Enter the number\n"))
# print("Factorial using iterative method",iterative_factorial(num))

# Below example is recursive method
def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)


num = int(input("Enter the number\n"))
print("Factorial using recursive method is : ", recursive_factorial(num))
