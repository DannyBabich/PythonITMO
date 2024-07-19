

from PyQt5 import QtCore, QtGui, QtWidgets
import city_search
import start_air_search

"""Класс отвечает за визуальный интерфейс (GUI)"""
class Ui_AirportSearch(object):
    def setupUi(self, AirportSearch):
        AirportSearch.setObjectName("AirportSearch")
        AirportSearch.resize(600, 500)
        AirportSearch.setMinimumSize(QtCore.QSize(600, 500))
        AirportSearch.setMaximumSize(QtCore.QSize(600, 500))
        AirportSearch.setStyleSheet("color: rgb(90, 95, 90);")
        self.main_window = QtWidgets.QWidget()
        self.main_window.setObjectName("main_window")
        self.label = QtWidgets.QLabel(self.main_window)
        self.label.setGeometry(QtCore.QRect(0, 50, 601, 43))
        font = QtGui.QFont()
        font.setFamily(".Arial Hebrew Desk Interface")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(90, 95, 90);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.search_airports = QtWidgets.QPushButton(self.main_window)
        self.search_airports.setGeometry(QtCore.QRect(100, 150, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search_airports.setFont(font)
        self.search_airports.setStyleSheet("color: rgb(90, 95, 90);")
        self.search_airports.setObjectName("search_airports")
        self.search_city = QtWidgets.QPushButton(self.main_window)
        self.search_city.setGeometry(QtCore.QRect(100, 250, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search_city.setFont(font)
        self.search_city.setStyleSheet("color: rgb(90, 95, 90);")
        self.search_city.setObjectName("search_city")
        AirportSearch.addWidget(self.main_window)
        self.airports = QtWidgets.QWidget()
        self.airports.setObjectName("airports")
        self.min_lat = QtWidgets.QLineEdit(self.airports)
        self.min_lat.setGeometry(QtCore.QRect(360, 40, 221, 21))
        self.min_lat.setObjectName("min_lat")
        self.max_lat = QtWidgets.QLineEdit(self.airports)
        self.max_lat.setGeometry(QtCore.QRect(360, 80, 221, 21))
        self.max_lat.setObjectName("max_lat")
        self.min_long = QtWidgets.QLineEdit(self.airports)
        self.min_long.setGeometry(QtCore.QRect(360, 120, 221, 21))
        self.min_long.setObjectName("min_long")
        self.max_long = QtWidgets.QLineEdit(self.airports)
        self.max_long.setGeometry(QtCore.QRect(360, 160, 221, 21))
        self.max_long.setObjectName("max_long")
        self.label_2 = QtWidgets.QLabel(self.airports)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 301, 21))
        self.label_2.setStyleSheet("color: rgb(90, 95, 90);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.airports)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 301, 21))
        self.label_3.setStyleSheet("color: rgb(90, 95, 90);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.airports)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 301, 21))
        self.label_4.setStyleSheet("color: rgb(90, 95, 90);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.airports)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 301, 21))
        self.label_5.setStyleSheet("color: rgb(90, 95, 90);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.search_airportsButton = QtWidgets.QPushButton(self.airports)
        self.search_airportsButton.setGeometry(QtCore.QRect(20, 200, 560, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search_airportsButton.setFont(font)
        self.search_airportsButton.setStyleSheet("color: rgb(90, 95, 90);")
        self.search_airportsButton.setObjectName("search_airportsButton")
        self.airport_Textoutput = QtWidgets.QTextBrowser(self.airports)
        self.airport_Textoutput.setGeometry(QtCore.QRect(20, 240, 560, 192))
        self.airport_Textoutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.airport_Textoutput.setObjectName("airport_Textoutput")
        self.back_airportsButton = QtWidgets.QPushButton(self.airports)
        self.back_airportsButton.setGeometry(QtCore.QRect(20, 430, 560, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back_airportsButton.setFont(font)
        self.back_airportsButton.setStyleSheet("color: rgb(90, 95, 90);")
        self.back_airportsButton.setObjectName("back_airportsButton")
        AirportSearch.addWidget(self.airports)
        self.city = QtWidgets.QWidget()
        self.city.setObjectName("city")
        self.label_6 = QtWidgets.QLabel(self.city)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 561, 21))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(90, 95, 90);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.city)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 561, 21))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(90, 95, 90);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.first_cityline = QtWidgets.QLineEdit(self.city)
        self.first_cityline.setGeometry(QtCore.QRect(20, 70, 561, 41))
        self.first_cityline.setObjectName("first_cityline")
        self.second_city_line = QtWidgets.QLineEdit(self.city)
        self.second_city_line.setGeometry(QtCore.QRect(20, 150, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.second_city_line.setFont(font)
        self.second_city_line.setObjectName("second_city_line")
        self.back_cityButton = QtWidgets.QPushButton(self.city)
        self.back_cityButton.setGeometry(QtCore.QRect(20, 360, 560, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back_cityButton.setFont(font)
        self.back_cityButton.setStyleSheet("color: rgb(90, 95, 90);")
        self.back_cityButton.setObjectName("back_cityButton")
        self.search_cityButton = QtWidgets.QPushButton(self.city)
        self.search_cityButton.setGeometry(QtCore.QRect(20, 200, 560, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search_cityButton.setFont(font)
        self.search_cityButton.setStyleSheet("color: rgb(90, 95, 90);")
        self.search_cityButton.setObjectName("search_cityButton")
        self.city_textOutput = QtWidgets.QTextBrowser(self.city)
        self.city_textOutput.setGeometry(QtCore.QRect(20, 240, 560, 121))
        self.city_textOutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.city_textOutput.setObjectName("city_textOutput")
        AirportSearch.addWidget(self.city)
        self.add_function()

        self.retranslateUi(AirportSearch)
        AirportSearch.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AirportSearch)

    def retranslateUi(self, AirportSearch):
        _translate = QtCore.QCoreApplication.translate
        AirportSearch.setWindowTitle(_translate("AirportSearch", "StackedWidget"))
        self.label.setText(_translate("AirportSearch", "ВЫБОР ЗАДАЧИ"))
        self.search_airports.setText(_translate("AirportSearch", "Поиск аэропортов в границах координат"))
        self.search_city.setText(_translate("AirportSearch", "Расчет расстояния между аэропортами городов"))
        self.label_2.setText(_translate("AirportSearch", "Укажите минимальную широту (min -180)"))
        self.label_3.setText(_translate("AirportSearch", "Укажите максимальную широту (max 180)"))
        self.label_4.setText(_translate("AirportSearch", "Укажите максимальную долготу (max 180)"))
        self.label_5.setText(_translate("AirportSearch", "Укажите минимальную долготу (min -180)"))
        self.search_airportsButton.setText(_translate("AirportSearch", "Поиск аэропортов в границах координат"))
        self.back_airportsButton.setText(_translate("AirportSearch", "Вернуться к начальному экрану"))
        self.label_6.setText(_translate("AirportSearch", "Введите название второго города (язык ввода Английский)"))
        self.label_7.setText(_translate("AirportSearch", "Введите название первого города (язык ввода Английский)"))
        self.back_cityButton.setText(_translate("AirportSearch", "Вернуться к начальному экрану"))
        self.search_cityButton.setText(_translate("AirportSearch", "Расчет расстояния между аэропортами городов"))

    def add_function(self):
        """Функция переключения между экранами виджета при нажатии кнопки"""
        self.search_airports.clicked.connect(self.search_airport)
        self.search_city.clicked.connect(self.search_city_f)
        self.search_airportsButton.clicked.connect(self.result_airports)
        self.search_cityButton.clicked.connect(self.result_city)
        self.back_cityButton.clicked.connect((self.backC))
        self.back_airportsButton.clicked.connect((self.backA))

    def search_airport(self):
        """Функция закрывает преидущее окно и открывает новое"""
        self.main_window.hide()
        self.airports.show()

    def search_city_f(self):
        """Функция закрывает преидущее окно и открывает новое"""
        self.main_window.hide()
        self.city.show()

    def backC(self):
        """Функция закрывает преидущее окно и открывает начальный экран"""
        self.city.hide()
        self.main_window.show()

    def backA(self):
        """Функция закрывает преидущее окно и открывает начальный экран"""
        self.airports.hide()
        self.main_window.show()


    def result_airports(self):
        """После вызова, функция обращается к модулю start_air_search с параметрами считанными из поллей ввода в GUI
        В случае если одно из полей не будет заполнено, функция выполнена не будет"""
        try:
            self.airport_Textoutput.setText(str(start_air_search.start_air_search(min_lat=float(self.min_lat.text()),
                                                                           max_lat=float(self.max_lat.text()),
                                                                           min_long=float(self.min_long.text()),
                                                                           max_long=float(self.max_long.text()))))
        except ValueError:
            pass

    def result_city(self):
        """После вызова, функция обращается к модулю city_search с параметрами считанными из поллей ввода в GUI
        В случае если одно из полей не будет заполнено, функция выполнена не будет"""
        try:
            self.city_textOutput.setText(str(city_search.city_search(first_city=(self.first_cityline.text()).title(),
                                                                     second_city=(self.second_city_line.text()).title())))

        except ValueError:
            pass



