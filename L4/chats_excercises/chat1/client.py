from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.56.1", 1234))

while True:
    data = input('Send >> ')
    client.sendall(data.encode())
    if data == 'exit':
        print('bye bye')
        client.close()
        break
    data =  client.recv(2048).decode()
    print(data)