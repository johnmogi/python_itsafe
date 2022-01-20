from better_math1 import *

while True:
    operator = input('enter an operator: +, -, *, :, to exit press x... ')
    if operator == 'x' :
        break
    if operator == '+':
        num1 = int(input('give me a number: '))
        num2 = int(input('give me a number: '))
        print(num1 + num2)

    if operator == '-':
        num1 = int(input('give me a number: '))
        num2 = int(input('give me a number: '))
        print(num1 - num2)

    if operator == '*':
        num1 = int(input('give me a number: '))
        num2 = int(input('give me a number: '))
        print(num1 * num2)

    if operator == ':':
        num1 = int(input('give me a number: '))
        num2 = int(input('give me a number: '))
        if num2 == 0 :
            print('cannot divide by 0...')
            continue
        print(num1 / num2)


