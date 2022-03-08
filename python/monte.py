import random
import math
import time

def approxpi(nthrows: float) -> float:
    inside = 0
    for i in range(nthrows):
        if math.hypot(random.random(), random.random()) <= 1:
            inside += 1
    return 4.0 * inside / nthrows
 
start = time.time()
print('pi: ',approxpi(100000000),' in: ', time.time() - start)
