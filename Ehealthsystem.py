def getdate():
    import datetime
    return datetime.datetime.now()


def log(b):
    if b == 1:
        c = int(input("Enter 1 for vaidu 2 for jaydeep 3 for nirjal\n"))
        if c == 1:
            f = open("diet_vaidu.txt","a")
            e = str(getdate())
            d = input("Type diet hear\n")
            f.write(e+" : "+d+"\n")
            f.close()
        elif c == 2:
            f = open("diet_jaydeep.txt","a")
            e = str(getdate())
            d = input("Type diet hear\n")
            f.write(e+" : "+d+"\n")
            f.close()
        elif c == 3:
            f = open("diet_nirjal.txt","a")
            e = str(getdate())
            d = input("Type diet hear\n")
            f.write(e+" : "+d+"\n")
            f.close()
        else:
            print("Enter the correct choice")
    if b == 2:
        g = int(input("Enter 1 for vaidu 2 for jaydeep 3 for nirjal\n"))
        if g == 1:
            f = open("exercise_vaidu.txt", "a")
            e = str(getdate())
            d = input("Type exercise hear\n")
            f.write(e + " : " + d + "\n")
            f.close()
        elif g == 2:
            f = open("exercise_jaydeep.txt", "a")
            e = str(getdate())
            d = input("Type exercise hear\n")
            f.write(e + " : " + d + "\n")
            f.close()
        elif g == 3:
            f = open("exercise_nirjal.txt", "a")
            e = str(getdate())
            d = input("Type exercise hear\n")
            f.write(e + " : " + d + "\n")
            f.close()
        else:
            print("Enter the correct choice")


def retrive(h):
    if h == 1:
        i = int(input("Enter 1 for vaidu 2 for jaydeep 3 for nirjal\n"))
        if i == 1:
            f = open("diet_vaidu.txt","r")
            print(f.read())
            f.close()
        elif i == 2:
            f = open("diet_jaydeep.txt","r")
            print(f.read())
            f.close()
        elif i == 3:
            f = open("diet_nirjal.txt","r")
            print(f.read())
            f.close()
        else:
            print("Enter the correct choice")

    elif h == 2:
        j = int(input("Enter 1 for vaidu 2 for jaydeep 3 for nirjal\n"))
        if j == 1:
            f = open("exercise_vaidu.txt","r")
            print(f.read())
            f.close()
        elif j == 2:
            f = open("exercise_jaydeep.txt","r")
            print(f.read())
            f.close()
        elif j == 3:
            f = open("exercise_nirjal.txt","r")
            print(f.read())
            f.close()
        else:
            print("Enter the correct choice")
    else:
        print("Enter the correct choice")


a = int(input("Enter 1 for log and 2 for retrive\n"))
if a == 1:
    b = int(input("Enter 1 for diet and 2 for exercise\n"))
    log(b)
elif a == 2:
    h = int(input("Enter 1 for diet and 2 for exercise\n"))
    retrive(h)
else:
    print("Enter the correct choice")

