import os

commands = []

for i in range(5):

    command = input("give me a command: ")
    commands.append(command)

for c in commands:
    ok = os.system(c)
    if ok == 0:
        try:
            print(os.popen(c).read())
        except Exception as e:
            print ('an error has occured: ', e)
# print(commands)