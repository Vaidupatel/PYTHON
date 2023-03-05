# Lambda function or anonymous function
# def add(a, b):
#     return a+b

# add = lambda a, b: a + b
#
# print(add(9, 900))


def a_first(a):
    return a[1]


a = [[1, 4], [55, 66], [8, 23]]
a.sort(key=a_first)
print(a)
