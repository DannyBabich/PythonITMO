from random import randint
import time

def gamers(x):
    gamers_lst = []
    for i in range(x):
        i = input('Введите имя игрока: ')
        gamers_lst.append(i)
    return gamers_lst


def game():
    players = gamers(q_gamers)
    score = {}
    for i in players:
        print('Кубик бросает ', i)
        time.sleep(2)
        n = []
        for j in range(attempt):
            j = randint(1, 6)
            n.append(j)
        score[i] = sum(n)
        print('Игрок ', i, ' набрал ', score[i], ' очков.')
    sorted_score = sorted(score.items(),key=lambda item: item[1], reverse=True)
    return print('Выйграл', sorted_score[0][0], '. Он набрал ', sorted_score[0][1], 'очков.')



q_gamers = int(input('Введите колличество игроков: '))
attempt = int(input('Введите колличество попыток для каждого игрока: '))

game()