import random
rand = random.randint(1,100)
tries = 0

while True:
    num = int(input("enter your guess: "))
    tries += tries + 1
    if num == rand :
        break
    
    if num > rand :
        print('hmm, your guess is too big', rand)
        continue

    if num < rand :
        print('hmm, your guess is too small', rand)
        continue

print('number of tries: ', tries -1)

