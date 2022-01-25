#num1 = int(input('enter a number: '))
#num2 = int(input('enter a number: '))
#if num1 > num2:
#    print ('the biggest number is num1:' , num1)
#elif num1 == num2:
#    print('numbers match...')
#else:
#    print ('the biggest number is num2:' , num2)

#lan = input('what\'s your favourite language? ')
#if lan == 'python':
#    print('you win')
#else:
#    print('you suck')



num1 = int(input('enter a number: '))
num2 = int(input('enter a number: '))

def sum(num1, num2):
    result = (num1 + num2)
    return result

result = sum(num1, num2)

while True:
    num3 = int(input('enter a smaller number then {0}: '.format(result)))
    if num3 <= result:
        print('wrong answer')
    else:
        print('correct')
        break