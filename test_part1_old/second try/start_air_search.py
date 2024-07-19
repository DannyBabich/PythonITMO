"""Модуль отвечает за операционную часть программы"""

class start_air_search:
    """Класс принимает четыре переменные (float), указанные пользователем в GUI"""
    def __init__(self, min_lat: float, max_lat: float, min_long:float, max_long:float):
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_long = min_long
        self.max_long = max_long


    def open_file(self):
        """Функция отвечает за открытия файла и прeобразование информации.
        Сохраняет и возвращает список информации считанной в файле"""
        import csv
        file = 'airports.csv'
        self.lst = []
        with open(file, 'r') as fl:
            reader = csv.reader(fl)
            for row in reader:
                for elem in row:
                    self.lst.append(elem.split('|'))
        return self.lst

    def model(self):
        """Через цикл функция производит поиск объектов в списке, полученном из функции open_file, соответствующих запросу пользователя.
        Сохраняет их в преобразованном виде в отдельный список"""
        final_lst = []
        for elem in self.open_file()[1:len(self.open_file()) - 1]:
                try:
                    if self.min_lat <= float(elem[6]) <=self.max_lat and self.min_long <= float(elem[7]) <= self.max_long:
                        final_lst.append([elem[2], elem[3], elem[6], elem[7]])
                    else:
                        continue
                except IndexError:
                    pass
        return ('\n'.join(map(str,(final_lst))))

    def __str__(self):
        """Функция возвращает строку с результатами работы модуля"""
        return f' Аэропорты следующих городов находятся в границах указанных Вами координат: \n {self.model()}'

