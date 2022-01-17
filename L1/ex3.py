#get 2 nums from user and print the biggest
# ask user for fav programming language - display error if not python
# ask user for 2 nums keep sum in third var
#@ - ask for added num that is smaller then sum

# num1 = int(input('give me the 1st number: '))
# num2 = int(input('give me the 1st number: '))

# if num1 > num2 :
#     print('num1 is bigger: ' , num1)
# else :
#     print('num2 is bigger: ' , num2)

# fav = input( 'your favourite programming language is: ')
# if fav != "python" :
#     print('you suck')
# else : 
#     print( 'your\'e the best' )

num1 = int(input('give me the 1st number: '))
num2 = int(input('give me the 1st number: '))
num3 = num1 + num2
print(num3)
num4 = int(input('give me the 3rd number, but make it smaller then the mentionned sum: '))
if num4 < num3 :
    print('great')
else :
    print('you suck')




