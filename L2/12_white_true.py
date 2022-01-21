import random
rand = random.randint(1,100)
tries = 0

fd = open('result.txt', 'w')

def exit():
    fd = open('result.txt', 'a')
    fd.seek(0)
    fd.write("number of attempts so far: ")
    fd.write(str(tries -1))
    fd.write("\n")
    print('see you soon...')

print('''
Wellcome to guess the number game.
if you want to exit the game press "-1".
if you want to save the game press "1001".
Enjoy...
''')

while True:

    num = int(input("enter your guess: "))
    tries += tries + 1
    if num == rand or num == -1 :
        exit()
        break

    if num == -2:
        exit()
        break

    if num > rand :
        print('hmm, your guess is too big', rand)
        continue

    if num < rand :
        print('hmm, your guess is too small', rand)
        continue

fd.close()
print('number of tries: ', tries -1)


