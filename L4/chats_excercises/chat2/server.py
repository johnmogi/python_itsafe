from socket import *
import multiprocessing

guests = []

server = socket(AF_INET, SOCK_STREAM)
server.bind(("192.168.56.1", 1234))
server.listen(5)

client,addr = server.accept()
guests.appent(client)
print ("Welcome {0}".format(addr))

def connectGuest():
    while True:

        data = client.recv(2048).decode()
        if data == 'exit':
            print('goodbye')
            client.close()
            break
        print ("I just received: {0}".format(data))
        client.sendall("Thanks".encode())

server.close()

if __name__ == '__main__':
    for guest in guests:
        p = multiprocessing.Process(target=connectGuest, )
        p.start()