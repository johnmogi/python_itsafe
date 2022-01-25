# guess the number - random num,
import random
attempts = 0

max = int(input('enter the max value for the game: '))
rand = random.randint(1,max)

while True:
    guess = int(input('guess a number between 1 and {0}: '.format(max)))

    if guess != rand:
        attempts = attempts + 1

    if guess < rand:
        print('number is too small ', rand)
    elif guess > rand:
        print('number is too big ', rand)
    else :
        break

print('you won!, number of attempts: ', attempts)
