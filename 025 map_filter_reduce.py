# ------------------------------------------------------ MAP FUNCTION
# a = ['3', '34', '34', '45']
#
# # To convert this string numbers in to integer we will apply the for loop
# # for i in range(len(number)):
# #     number[i] = int(number[i])
#
# # But we can do this thing easily using map function
# d = list(map(int, a))       # We have to convert map function in to the list and store in any variable
# d[2] = d[2] + 1
# print(d[2])
#
# # OTHER EXAMPLE to return the square of the given list
#
#
# # def sq(a):    # We can use the lambada function behalf of this
# #     return a*a
#
#
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # square = list(map(sq, l1))                # Using the function sq
# square = list(map(lambda x: x*x, l1))       # Using the lambada function
# print(square)


# def square(a):
#     return a*a
#
#
# def cube(a):
#     return a*a*a
#
#
# funcs = [square, cube]
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in l1:
#     # That mean there is function called x which takes 'funcs' (which is the list of function) as input,
#     # and return the value which will return by function, hear x will take an input funcs,
#     # and because there is two function are there in list it will execute bot the function present in the list one by one
#     # for given values
#     val = list(map(lambda x: x(i), funcs))
#     print(val)



# -----------------------------------------------------FILTER FUNCTION
# list_1 = l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def is_greater(num):
#     return num>5
#
#
# gr_than_5 = list(filter(is_greater, list_1))
# print(gr_than_5)

# ---------------------------------------------------REDUCE FUNCTION

list_1 = l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# num = 0
# for i in list_1:
#     num = num+i
# print(num)
# We can do this thing in one line using reduce function
from functools import reduce
num = reduce(lambda x, y: x*y, list_1)
print(num)
