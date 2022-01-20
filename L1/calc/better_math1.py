def calculator( num1, num2, operator):
    if operator == '+':
        return num1+ num2
    elif operator == '-':
        return (num1 - num2)
    elif operator == '*':
        return (num1 * num2)
    elif operator == ':':
        if num1 == 0 or num2 == 0:
             return 'one of the numbers is 0... try again'
        else:
            return int( num1 / num2)
