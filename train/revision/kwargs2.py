def calculator(**kwargs):
    if 'action' in kwargs:
        if kwargs['action'] == 'add':
            num1 = kwargs['num1']
            num2 = kwargs['num2']
            result = num1 + num2
            return result

if __name__ == '__main__':
    print(calculator(action='add', num1 = 1, num2 = 3))