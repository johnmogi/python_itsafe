import os

commands = []

for i in range(5):
    command = input("give me a command: ")
    commands.append(command)

for c in commands:
    print(os.popen(c).read())
    #os.popen(c).read()

# print(commands)