import random

num=random.randint(1,30)

while True:

    guess=int(input("Enter a number between 1 to 30: "))

    if guess==num:
        print("You choose correct number")
        break
    elif guess>num:
        print("You choose greater number")
    elif guess<num:
        print("You choose smaller number")
