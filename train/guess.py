import os.path

from run import start, rand



# check if db file exists:
is_db = os.path.isfile('db.txt')
if is_db != True:
    db = open('db.txt', 'w')

start()

# save state:
with open('result.txt', 'w') as fd:
    fd.write(str(rand))
    fd.write('|')
    fd.write(str(tries))
