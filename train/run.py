import random
rand = random.randint(1,100)

def start():
    tries = 0
    menu = input('press [s] to start, [l] to load last game, [x] to exit...')
    if menu == 'x':
        print('goodbye')
        exit(0)
#    elif menu == 'l':
#        pass
    scope =  int(input('enter a number for maximum value... '))

    while True:
        guess = int(input('enter a number from 1-{0} '.format(scope)))
        if guess < rand:
            tries += tries
            print('your number is too small... ', rand)
            continue
        if guess > rand:
            print('your number is too big... ', rand)
            continue
        else:
            print('Congratulations, you won! ', rand)
            exit(0)


    return guess, scope, tries

if __name__ == "__main__":
    start()