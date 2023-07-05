import random
import time

start_time = time.time()

for i in range(1000000):
    base = random.randint(1000000, 10000000)
    exp = random.randint(1, 100)
    pow(base, exp)

end_time = time.time()

print('Time taken:', end_time - start_time, 'seconds')