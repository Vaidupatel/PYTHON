# def func1():
#     print('hello guys')
#
# func2 = func1       # it will copy func1() in func2()
# del func1           # How evere func1 will deleted, but there is copy of func1 in func2
# func2()

# def funcret(num):
#     # print and sum are built in function
#     # We can return a function through the function
#     if num ==0:
#         return print
#     if num == 1:
#         return sum
#
#
# a = funcret(1)
#
# print(a)


# def execute(func):
#     # We can pass function through function and execute
#     func('this will print through the  print function pass in execute function')
#
#
# execute(print)

def dec1(func1):
    def nowexe():
        print('now executing')
        func1()
        print('executed')
    return nowexe


@dec1       # This is short method for writing 'vaid = dec1(vaid)'
def vaid():
    print('vaidu is good boy')

# Function vaid will pass in to dec1 as a func1
# First nowexe will execute and thane print execute, func1 execute, print execute and nowexe will return


# vaid = dec1(vaid)

vaid()
