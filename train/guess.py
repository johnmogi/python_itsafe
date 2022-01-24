import os.path

from run import start, rand

# check if db file exists:
is_db = os.path.isfile('db.txt')
if is_db != True:
    db = open('db.txt', 'w')
    tries =0
else:
    db = open('db.txt', 'r')
    db.read().find('|')

db.close()


start()


