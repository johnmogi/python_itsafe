#ask user to give 5 nums 1-5
# save into a list
#if the user added an illegeal num-
# display an error + reject num 
# print list

num1 = int(input('give me 1 '))
num2 = int(input('give me 2 '))
num3 = int(input('give me 3 '))
num4 = int(input('give me 4 '))
num5 = int(input('give me 5 '))
# numbers = [num1,num2,num3,num4,num5]
numbers = []
if num1 != 1 :
    print('incorrect number 1')
else:
    numbers.append(num1)

if num2 != 2 :
    print('incorrect number 2')
else:
    numbers.append(num2)

if num3 != 3 :
    print('incorrect number 3')
else:
    numbers.append(num3)

if num4 != 4 :
    print('incorrect number 4')
else:
    numbers.append(num4)

if num5 != 5 :
    print('incorrect number 5')
else:
    numbers.append(num5)



print(numbers)