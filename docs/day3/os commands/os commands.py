import os


commands = []
for i in range(5):
    command = input("Give me a command > ")
    commands.append(command)

print ("[*] executing the commands")

for command in commands:
    if os.system(command) == 0:
        print ("[+] Command '{0}' success".format(command))
    else:
        print("[-] Command '{0}' fail".format(command))