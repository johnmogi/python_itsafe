import os


def get_ip_v2():
    ip = os.popen("netsh interface ip show address")
    for line in ip.readlines():
        if "IP Address" in line:
            start = line.rfind(" ")
            break

    return line[start:-1]

print(get_ip_v2())