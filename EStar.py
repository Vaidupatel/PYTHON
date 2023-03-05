print("Pattern printing")
num = int(input("How many roy you want to print?\n"))
a = input("Press 1 for forward Press 0 for revers\n")
if a == "1":
    for i in range(0, num+1):
        print("*"*i)
if a == "0":
    for i in range(num, 0, -1):
        print("*"*i)

