# guees the number game:

import random
rand = random.randint(1,1000)

# user guesses the result
# for each try he will get feedback if it's higher or lower

# success : print number of attempts.
attempts = 0
guess = 0

print('''

            
נחשו את המספר של דה שון דה חתולי:
                       /)
              /\___/\ ((
              \`@_@'/  ))
              {_:Y:.}_//
    ----------{_}^-'{_}----------
    רמז: 1-1,000
    בהצלחה!
            ''')
while rand != guess :
    guess = int(input('מה הניחוש שלכם? תנו לי מספר... '))
    attempts=+attempts + 1
    if guess < rand:
        print('המספר שלכם קטן מדי! נסו שנית')
    else:
        print('המספר שלכם גדול מדי! נסו שנית')
    print("מספר ניסיונות: ", attempts)
    continue

print('''
            הצלחה!
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
''')

# while guess < rand or guess > rand :
#    if guess < rand:
#        print('your guess is smaller then the desired number')
#    elif guess > rand:
#        print('your guess is bigger then the desired number')
#        continue
#    attempts += attempts

