def calculator(**kwargs):
    if 'action' in kwargs:
        num1 = kwargs['num1']
        num2 = kwargs['num2']

        if kwargs['action'] == '+':
            result = num1 + num2
            return result
        elif kwargs['action'] == '-':
            result = num1 - num2
            return result
        elif kwargs['action'] == '*':
            result = num1 * num2
            return result
        elif kwargs['action'] == ':':
            try:
                result = num1 / num2
                return result
            except:
                if num2 == 0:
                    print('err: 0 division')

if __name__ == '__main__':
    print(calculator(action='+', num1 = 1, num2 = 3))