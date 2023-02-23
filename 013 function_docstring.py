print("Enter the number 1")
num1=input()
print("Enter the number 2")
num2=input()
try:
    print("The sun of two number is ",int(num1)+int(num2))
except Exception as e:
    print(e)    
print("This line show how try except exception is work")
