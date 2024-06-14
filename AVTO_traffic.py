
from random import random
def start_traffic(a,b):
    while a:
    # decrease time
        a -= 1
        print('')
        move(b)

def move(x):
    for i in range(len(x)):
        # move car
        if random() > 0.3:
            x[i] += 1

        # draw car
        print('-' * x[i])

time = 5
car_positions = [1, 1, 1]

start_traffic(time, car_positions)

