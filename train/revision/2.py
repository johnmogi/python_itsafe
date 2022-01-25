# ask user for a num between 1-5, if exception don't put it in the list

numbers = []

for i in range(5):
    num = int(input('enter a number, value 1-5: '))
    if 1 < num < 5 :
        numbers.append(num)

print(numbers)