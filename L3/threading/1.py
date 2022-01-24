import time
import threading

num1 = 1
num2 = 1000
start = time.time()
threads = []

def counter(number):
    for num1 in range(number):
        print(num1)

for num1 in range(5):
    t = threading.Thread(target=counter, args =(100000,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end = time.time() - start
print('time it took: ', end)
# 2.952414035797119
