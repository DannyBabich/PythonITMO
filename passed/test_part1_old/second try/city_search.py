"""Модуль отвечает за операционную часть программы в части определения расстояния между городами"""

class city_search:
    """Класс принимает две переменные (str), указанные пользователем в GUI"""
    def __init__(self, first_city: str, second_city: str):
        self.first_city = f'"{first_city}"'
        self.second_city = f'"{second_city}"'



    def open_file(self):
        """Функция отвечает за открытия файла и прeобразование информации.
        Сохраняет и возвращает список информации считанной в файле"""
        import csv
        file = 'airports.csv'
        lst = []
        with open(file, 'r') as fl:
            reader = csv.reader(fl)
            for row in reader:
                for elem in row:
                    lst.append(elem.split('|'))
        return lst

    def model(self):
        """функция осуществляет поиск по списку возвращенного из функции open_file"""
        from haversine import haversine
        city_1 = ()
        city_2 = ()
        for elem in self.open_file():
            try:
                if elem[2] == self.first_city:
                    city_1 = (float(elem[6]), float(elem[7]))
                if elem[2] == self.second_city:
                    city_2 = (float(elem[6]), float(elem[7]))
            except:
                continue

        distance = haversine(city_1, city_2)
        return distance

    def __str__(self):
        """Функция возвращает строку с результатами работы модуля"""
        return f' Расстояние между городами{self.first_city} и {self.second_city}: {self.model(): .2f} километров'

