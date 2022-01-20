def calculator(num1=0, num2 = 0, *args):
    if args is None:
        return "please provide arguments..."
    else :
        for arg in args:
            if arg == '+':
                result = (num1 + num2)
                return result

            if arg == '-':
                result = (num1 - num2)
                return result

            if arg == '*':
                result = (num1 * num2)
                return result

            if arg == ':':
                if num1 == 0 or num2 == 0:
                    print('one of the numbers is 0... try again')
                else:
                    result = (num1 / num2)
                    return result