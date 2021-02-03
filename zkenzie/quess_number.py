import random

def guess(x):
    num = random.randint(1,x)
    guess = 0
    tries = 3

    while guess != num:
        if tries == 0:
            break
        elif guess < num:
            print(f"sorry try again. too low. you have {tries} chances remaining ")
        elif guess > num:
            print("sorry, try again. number too high. ")
        else:
            print("correct! you guessed right!!")
        guess = int(input(f"pick a number between 1 and {x}: "))
        tries -= 1


guess(10)