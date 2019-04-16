print("""


Guess a number between 1-40.


""")



import random
import time



rand_num = random.randint(1,40)

chance = 7

while True:

    guess = int(input("Number:\n"))


    if guess < rand_num:
        print("Numbers running...\n")
        time.sleep(1)

        print("Guess a bigger number.")
        chance -= 1


    elif guess > rand_num:
        print("Numbers running...\n")
        time.sleep(1)

        print("Guess a smaller number.")
        chance -= 1


    else:
        print("Numbers running...\n")
        time.sleep(1)

        print("CORRECT!\n")
        break

    if chance == 0:
        print("You have failed.\n")
        print("Number was:\n")
        time.sleep(1)
        print(rand_num, "\n")
        break

    if guess > 40:
        print("Guess a number between 1-40!")
        chance -= 1
















