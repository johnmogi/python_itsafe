import time
import threading

start_time = time.time()

def counter(number):
  for number in range(1000):
        number = number +1
        print(number)

for i in range(5):
    counter(1)

print('time it took: ', ( time.time() - start_time))