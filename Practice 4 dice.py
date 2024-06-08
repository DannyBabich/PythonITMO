# -*- coding: utf-8 -*-

#1 Создайте программу
import random
from random import randint
import time

gamer1 = input('Введите имя первого игрока ')
gamer2 = input('Введите имя второго игрока ')

print('Кубик бросает ', gamer1)

time.sleep(2)
n1 = randint(1,6)
print('Выпало число: ', n1)

print('Кубик бросает ', gamer2)

time.sleep(2)
n2 = randint(1,6)
print('Выпало число: ', n2)

if n1>n2:
  print('Выйграл ', gamer1)
elif n1<n2:
  print('Выйграл ', gamer2)
else:
  print('Ничья')

#2 дополнить циклом
from random import randint
import time

gamer1 = input('Введите имя первого игрока ')
gamer2 = input('Введите имя второго игрока ')
attempt = int(input('Ведите колличество попыток '))

print('Кубик бросает ', gamer1)

time.sleep(5)
n1 = 0
for i in range(0,attempt):
  i = randint(1,6)
  n1 += i
print('Игрок ', gamer1, ' набрал ', n1, ' очков.')

print('Кубик бросает ', gamer2)

time.sleep(5)
n2 = 0
for i in range(0,attempt):
  i = randint(1,6)
  n2 += i
print('Игрок ', gamer2, ' набрал ', n2, ' очков.')

if n1>n2:
  print('Поздравляем! Выйграл ', gamer1)
elif n1<n2:
  print('Поздравляем! Выйграл ', gamer2)
else:
  print('Ничья')

#3
"""Дополнить словарем (в словаре сохранены результаты бросков,
можно дополнить колличеством бросков, и т.д.)"""

from random import randint
import time

gamer1 = input('Введите имя первого игрока ')
gamer2 = input('Введите имя второго игрока ')
attempt = int(input('Ведите колличество попыток '))

g1 = {}
g2 = {}

print('Кубик бросает ', gamer1)

time.sleep(5)
n1 = []
for i in range(0,attempt):
  i = randint(1,6)
  n1.append(i)
g1[gamer1] = n1
print('Игрок ', gamer1, ' набрал ', sum(n1), ' очков.')

print('Кубик бросает ', gamer2)

time.sleep(5)
n2 = []
for i in range(0,attempt):
  i = randint(1,6)
  n2.append(i)
g2[gamer2] = n2
print('Игрок ', gamer2, ' набрал ', sum(n2), ' очков.')

if sum(n1)>sum(n2):
  print('Поздравляем! Выйграл ', gamer1, '. Статистика бросков:', g1)
elif sum(n1)<sum(n2):
  print('Поздравляем! Выйграл ', gamer2, '. Статистика бросков:',  g2)
else:
  print('Ничья')

