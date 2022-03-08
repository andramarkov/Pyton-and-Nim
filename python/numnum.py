#https://www.reddit.com/r/learnpython/comments/ahy84c/can_i_make_estimating_pi_with_the_monte_carlo/

import time
import numpy as np

def approxpi(nthrows: float) -> float:
    inside = 0
    inside = np.sum(np.random.rand(nthrows)**2 + np.random.rand(nthrows)**2 <= 1)
    return 4 * inside / nthrows

start = time.time()
print('pi: ',approxpi(100000000),' in: ', time.time() - start)

