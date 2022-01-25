from kwargs2 import calculator

sum = calculator(action='+', num1 = 2, num2 = 4)
sub = calculator(action='-', num1 = 2, num2 = 4)
mul = calculator(action='*', num1 = 2, num2 = 4)
div = calculator(action=':', num1 = 2, num2 = 0)

print(sum, sub, mul, div)