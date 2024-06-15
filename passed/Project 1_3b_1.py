import random
from random import randint
lst = [randint(0,100) for i in range(0,20)]

value = int(input('Введите любое число от 0 до 100 '))

lst2 = []

for i in lst:
    if i > value:
        lst2.append('High')
    elif i < value:
        lst2.append('Low')
    else:
        lst2.append('Equals')

print(lst)
print(lst2)