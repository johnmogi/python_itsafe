import os

# dir = os.system('dir')
ip = os.popen('ipconfig')

for line in ip.readlines():
    print(line)   