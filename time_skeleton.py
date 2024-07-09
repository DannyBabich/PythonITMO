import time

'''Первый вариант кода реализован через получение из модуля time текущего времени (часов, минут и секунд)
   Полученные значения передаются в класс TIME.
   Без преобразования возвращаются через метод __str__'''
class Time(object):
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def convert(self):
        pass

    def __str__(self):
         return f'{self.hr}:{self.min}:{self.sec} '

    def __add__(self, other):
         pass

    def __sub__(self, other):
        pass


if __name__ == '__main__':
    now = Time(time.strftime('%H'),  time.strftime('%M'), time.strftime('%S'))
    print(now)


'''Второй вариант кода реализован через получение из модуля time секунд от начала эры.
   Полученные значения преобразуются в строку в модуле convert.
   И возвращаются пользователю через метод __str__'''

class Time2(object):
    def __init__(self, sec: float):
        self.sec = sec

    def convert(self) -> str:
        converted_time = time.ctime(self.sec)
        military_time = converted_time.split()[-2]
        return military_time

    def __str__(self):
        return  f'{self.convert()}'

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass


if __name__ == '__main__':
    now2 = Time2(time.time())
    print(now2)



'''Третий вариант кода реализован через ввод времени через функцию input.
   Полученные значения проверяются в модуле convert. И если превышают общепринятое значение, обнуляются
   Функция __add__ дополняет часы разделителем ':'
   Данные возвращаются пользователю через метод __str__
   В коде присутствует 6 простых тестов на корректность ввода данных'''

class Time3(object):
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def convert(self):
        if self.hr > 23:
            self.hr = '00'
        if self.min > 59:
            self.min = '00'
        if self.sec > 59:
            self.sec = '00'

    def __str__(self):
        self.convert()
        return  f'{self.hr}{self.__add__()}{self.min}{self.__add__()}{self.sec}'

    def __add__(self):
        points = ':'
        return points

    def __sub__(self, other):
        pass


if __name__ == '__main__':
    hr = int(input('Введите часы: '))
    min = int(input('Введите минуты: '))
    sec = int(input('Введите секунды: '))
    now3 = Time3(hr, min, sec)
    print(now3)

    assert hr < 24, f'Введено число превышающее количество часов в сутках: {hr}'
    assert min < 60, f'Введено число превышающее количество минут в часах: {min}'
    assert hr < 60, f'Введено число превышающее количество секунд в минуте: {sec}'

