num1=float(input("Enter the number 1"))
op=input("Enter the operator")
num2=float(input("Enter number 2"))

if num1==45 and num2==3 and op=='*':
    print("555")
elif num1==56 and num2==9 and op=='+':
    print("77")
elif num1==56 and num2==6 and op=='/':
    print("4")
elif op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
else:
    print("Enter valid operator")
