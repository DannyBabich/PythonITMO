
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
import start_air_search
import city_search

"""Класс отвечает за визуальный интерфейс (GUI)"""
class Ui_StackedWidget(object):


    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(420, 491)
        self.main_window = QtWidgets.QWidget()
        self.main_window.setObjectName("main_window")
        self.label = QtWidgets.QLabel(self.main_window)
        self.label.setGeometry(QtCore.QRect(0, 20, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(90, 95, 90);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.main_window)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(91, 91, 91);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.main_window)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(91, 91, 91);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.search_Button_1 = QtWidgets.QPushButton(self.main_window)
        self.search_Button_1.setGeometry(QtCore.QRect(60, 150, 300, 50))
        self.search_Button_1.setObjectName("search_Button_1")
        self.search_Button_2 = QtWidgets.QPushButton(self.main_window)
        self.search_Button_2.setGeometry(QtCore.QRect(60, 290, 300, 50))
        self.search_Button_2.setObjectName("search_Button_2")
        StackedWidget.addWidget(self.main_window)
        self.airports = QtWidgets.QWidget()
        self.airports.setObjectName("airports")
        self.min_lat = QtWidgets.QLineEdit(self.airports)
        self.min_lat.setGeometry(QtCore.QRect(60, 50, 300, 30))
        self.min_lat.setObjectName("min_lat")
        self.max_lat = QtWidgets.QLineEdit(self.airports)
        self.max_lat.setGeometry(QtCore.QRect(60, 110, 300, 30))
        self.max_lat.setObjectName("max_lat")
        self.min_long = QtWidgets.QLineEdit(self.airports)
        self.min_long.setGeometry(QtCore.QRect(60, 170, 300, 30))
        self.min_long.setObjectName("min_long")
        self.max_long = QtWidgets.QLineEdit(self.airports)
        self.max_long.setGeometry(QtCore.QRect(60, 230, 300, 30))
        self.max_long.setObjectName("max_long")
        self.outputText_airpirts = QtWidgets.QTextBrowser(self.airports)
        self.outputText_airpirts.setGeometry(QtCore.QRect(20, 311, 381, 151))
        self.outputText_airpirts.setObjectName("outputText_airpirts")
        self.serch_airportsButton = QtWidgets.QPushButton(self.airports)
        self.serch_airportsButton.setGeometry(QtCore.QRect(150, 270, 113, 32))
        self.serch_airportsButton.setObjectName("serch_airportsButton")
        self.label_4 = QtWidgets.QLabel(self.airports)
        self.label_4.setGeometry(QtCore.QRect(60, 20, 300, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.airports)
        self.label_5.setGeometry(QtCore.QRect(60, 80, 300, 30))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.airports)
        self.label_6.setGeometry(QtCore.QRect(60, 140, 300, 30))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.airports)
        self.label_7.setGeometry(QtCore.QRect(60, 200, 300, 30))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        StackedWidget.addWidget(self.airports)
        self.city = QtWidgets.QWidget()
        self.city.setObjectName("city")
        self.label_8 = QtWidgets.QLabel(self.city)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 401, 50))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.city)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 401, 50))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.search_cityButton = QtWidgets.QPushButton(self.city)
        self.search_cityButton.setGeometry(QtCore.QRect(100, 220, 200, 50))
        self.search_cityButton.setObjectName("search_cityButton")
        self.outputText_city = QtWidgets.QTextBrowser(self.city)
        self.outputText_city.setGeometry(QtCore.QRect(10, 280, 401, 192))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.outputText_city.setFont(font)
        self.outputText_city.setObjectName("outputText_city")
        self.firstCityLine = QtWidgets.QLineEdit(self.city)
        self.firstCityLine.setGeometry(QtCore.QRect(20, 70, 381, 31))
        self.firstCityLine.setObjectName("firstCityLine")
        self.secondCityLine = QtWidgets.QLineEdit(self.city)
        self.secondCityLine.setGeometry(QtCore.QRect(20, 160, 381, 31))
        self.secondCityLine.setObjectName("secondCityLine")
        StackedWidget.addWidget(self.city)
        self.add_function()

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)


    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.label.setText(_translate("StackedWidget", "Что будем делать?"))
        self.label_2.setText(_translate("StackedWidget", "Поиск аэропортов в границах координат"))
        self.label_3.setText(_translate("StackedWidget", "Расчет расстояния между городами"))
        self.search_Button_1.setText(_translate("StackedWidget", "ПОИСК"))
        self.search_Button_2.setText(_translate("StackedWidget", "ПОИСК"))
        self.serch_airportsButton.setText(_translate("StackedWidget", "ПОИСК"))
        self.label_4.setText(_translate("StackedWidget", "Укажите минимальную широту (min -180)"))
        self.label_5.setText(_translate("StackedWidget", "Укажите максимальную широту (max 180)"))
        self.label_6.setText(_translate("StackedWidget", "Укажите минимальную долготу (min -180)"))
        self.label_7.setText(_translate("StackedWidget", "Укажите максимальную долготу (max 180)"))
        self.label_8.setText(_translate("StackedWidget", "Введите название первого города (язык ввода Английский)"))
        self.label_9.setText(_translate("StackedWidget", "Введите название второго  города (язык ввода Английский)"))
        self.search_cityButton.setText(_translate("StackedWidget", "ПОИСК"))

    def add_function(self):
        """Функция переключения между экранами виджета при нажатии кнопки"""
        self.search_Button_1.clicked.connect(self.search_airports)
        self.search_Button_2.clicked.connect(self.search_city)
        self.serch_airportsButton.clicked.connect(self.result_airports)
        self.search_cityButton.clicked.connect(self.result_city)

    def search_airports(self):
        """Функция закрывает преидущее окно и открывает новое"""
        self.main_window.hide()
        self.airports.show()

    def search_city(self):
        """Функция закрывает преидущее окно и открывает новое"""
        self.main_window.hide()
        self.city.show()


    def result_airports(self):
        """После вызова, функция обращается к модулю start_air_search с параметрами считанными из поллей ввода в GUI
        В случае если одно из полей не будет заполнено, функция выполнена не будет"""
        try:
            self.outputText_airpirts.setText(str(start_air_search.start_air_search(min_lat=float(self.min_lat.text()),
                                                                           max_lat=float(self.max_lat.text()),
                                                                           min_long=float(self.min_long.text()),
                                                                           max_long=float(self.max_long.text()))))
        except ValueError:
            pass

    def result_city(self):
        """После вызова, функция обращается к модулю city_search с параметрами считанными из поллей ввода в GUI
        В случае если одно из полей не будет заполнено, функция выполнена не будет"""
        try:
            self.outputText_city.setText(str(city_search.city_search(first_city=(self.firstCityLine.text()).title(),second_city=(self.secondCityLine.text()).title())))

        except ValueError:
            pass


