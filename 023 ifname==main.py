def vaidu(string):
    return f"This is a string{string}"


def add(num1, num2):
    return num1 + num2 + 5


print("And the name is ",__name__)

# if __name__ == '__main__': this is similar to the checking the condition "if name== main",
# because if we are executing the file whose function are ot imported from other file than that function hase name main
# and thus the condition checking that if__name__=='__main__' than  execute file
# if we are at file which is importing the function of other file than in present file name of that function will be
# the name of imported file rather than main
if __name__ == '__main__':
    print(vaidu("devanshi"))
    o = add(5, 6)
    print(o)
