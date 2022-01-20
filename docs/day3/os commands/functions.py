import os


# this function return the ip address of the system
def get_ip():
    ip =  os.popen("ipconfig")
    for line in ip.readlines():
        if "IPv4 Address" in line:
            start = line.find(":")
            end = -1
            output = line[start+2:end]
            break

    return output


# version 2 of get_ip, this function is good if get_ip not working for you
def get_ip_v2():
    ip = os.popen("netsh interface ip show address")
    for line in ip.readlines():
        if "IP Address" in line:
            start = line.rfind(" ")
            break

    return line[start:-1]


# version 3 of get_ip this is just another version, this version return a list of ips
def get_ip_v3():
    ip_list = []
    ip=os.popen("wmic NICCONFIG WHERE IPEnabled=true GET IPAddress")
    for line in ip.readlines():
        if "{" in line:
            start = line.find('"')+1
            end = line[start:].find('"') + start
            ip_list.append(line[start:end])

    return ip_list


if __name__ == '__main__':
    # this function return the ip address of the system
    print(get_ip())
    #print(get_ip_v2())
    #print(get_ip_v3())
