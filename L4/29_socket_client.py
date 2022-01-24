from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(("0.0.0.0", 1234))
server.listen(5)

client,addr = server.accept()
print ("Welcome {0}".format(addr))

while True:
    data = client.recv(2048).decode()
    print ("I just received: {0}".format(data))
    if data == 'exit':
        client.close()
        break

    client.sendall("Thanks".encode())
server.close()
