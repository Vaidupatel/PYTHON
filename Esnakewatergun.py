import random


def RNum():
    x = random.randrange(1, 4)

    return x


com_count = 0
user_count = 0
i = 0
while i != 10:

    n = int(input("Enter 1 for snake 2 for water 3 for gun\n"))
    com = RNum()
    print(com)
    if n == 1:
        print("You chose snake")
    elif n == 2:
        print("You chose water")
    elif n == 3:
        print("You chose gun")
    else:
        print("Enter the valid option")

    if n == 1 and com == 1:
        print("Computer choose snake")
        print("Game Draw")
    elif n == 1 and com == 2:
        print("Computer choose water")
        print("You won")
        user_count = user_count+1
    elif n == 1 and com == 3:
        print("Computer choose gun")
        print("Computer won")
        com_count = com_count+1
    elif n == 2 and com == 1:
        print("Computer choose snake")
        print("Computer won")
        com_count = com_count + 1
    elif n == 2 and com == 2:
        print("Computer choose water")
        print("Game Draw")
    elif n == 2 and com == 3:
        print("Computer choose gun")
        print("You won")
        user_count = user_count + 1
    elif n == 3 and com == 1:
        print("Computer choose snake")
        print("You won")
        user_count = user_count + 1
    elif n == 3 and com == 2:
        print("Computer choose water")
        print("Computer won")
        com_count = com_count + 1
    elif n == 3 and com == 3:
        print("Computer choose water")
        print("Game Draw")
    i += 1

print("Computer score:: ", com_count)
print("Your score:: ", user_count)
if com_count == user_count:
    print("Game draw")
elif com_count > user_count:
    print("Computer won")
elif com_count < user_count:
    print("User won")
