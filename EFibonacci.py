def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    pass


num = int(input("Enter the number to find fibonacci\n"))
print(fib(num))
