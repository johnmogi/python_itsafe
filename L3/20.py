try:
    num = int(input("give me a number: "))
    print(10 / num)
# except:
except Exception as e:
    print('Error', e)
    with open('error.log', 'a') as fd:
        fd.write(str(e) + '\n')
else:
    print('this happens only if it tries...')
finally:
    print('this allways happens...')
