import random

rand = random.randint(1,1000)
tries = 0
while True:
        user_guess = int(input("What is the number ? > "))
        if user_guess == rand:
                break

        elif user_guess > rand:
                print("Your number is bigger")
                tries += 1
        else:
                print("Your number is lower")
                tries += 1

print ("You win in {0} tries".format(tries))
