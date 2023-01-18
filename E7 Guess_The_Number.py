n=48
count=0
for i in range(5):
    g=int(input("Guess the number\n"))
    count=count + 1
    if 10>=g>=0:
        print("Your number is very very smaller ")
    elif 20>=g>10:
        print("Your number is very smaller")
    elif 30>=g>20:
        print("Your number is smaller")
    elif 40>=g>30:
        print("Your number is smaller but closer")
    elif 50>=g>40:
        if g==48:
            print("Yuppp!! you guess correct number")
            print("You have only ",4-i," left")
            break
        elif 45>=g>40 and g!=48:
            print("Your number is little bit smaller")
        elif 50>=g>45 and g!=48:
            print("Your number is little bit greater ")
    elif 60>=g>50:
        print("Your number is greater but closer")
    elif 70>=g>60:
        print("Your number is greater but closer")
    elif 80>=g>70:
        print("Your number is greater but not closer")
    elif 90>=g>80:
        print("Your number is very greater")
    elif 100>=g>90:
        print("Your number is very very greater")
    print("You have only ",4-i,"try left")

print("You guess number in ",count," try")
