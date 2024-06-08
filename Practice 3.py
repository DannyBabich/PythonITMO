
import random
from random import randint
lst = [randint(0,100) for i in range(0,10)]
print(lst)

import math
print(math.fsum(lst))

import statistics
print(statistics.mean(lst))
print(statistics.median(lst))
print(statistics.stdev(lst))

print(random.choice(lst))
print(random.sample(lst, 4))
