import random
rand = random.randint(1,100)
tries = 0


def bail():
    with open('result.txt', 'w') as fd:
        fd.seek(0)
        fd.write("number of attempts so far: ")
        fd.write(str(tries -1))
        fd.write("\n")
        print('see you soon...')
        exit(0)

def load():
    with open('result.txt', 'a') as loadFile:
        lines = loadFile.readlines()
        for line in lines:
            result = line.find[': ']
        print(result)


print('''
Wellcome to guess the number game.
Options menu: press [L] to load previous game.
press [x] to exit.
enjoy
''')

while True:

    num = input("enter your guess: ")
    tries += tries + 1
    if num == 'x':
        exit(0)

    if num == 's' :
        bail()

    if num == 'l':
        load()

    num = int(num)
    if num == rand:
        print('SUCCESS')
        bail()

    if num > rand :
        print('hmm, your guess is too big', rand)
        continue

    if num < rand :
        print('hmm, your guess is too small', rand)
        continue


print('number of tries: ', tries -1)


