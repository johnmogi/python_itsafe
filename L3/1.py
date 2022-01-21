fd = open('test.txt', 'a')
fd.write('Hello World\n')

fd.close

readFile = open('test.txt', 'r')
# print(readFile.read().split('\n'))
# lines = readFile.read().split('\n')
# for line in lines :
#    print(line)
readFile.seek(10,0)
print(readFile.read())
print(readFile.tell())
# truncate - deletes...


readFile.close()