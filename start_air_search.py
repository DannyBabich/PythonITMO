class start_air_search:
    def __init__(self,min_lat: float, max_lat: float, min_long:float, max_long:float):
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_long = min_long
        self.max_long = max_long

    def converter(self):
        self.convert_lst = self.open_file()
        return self.convert_lst

    def open_file(self):
        import csv
        file = 'airports.csv'
        self.lst = []
        with open(file, 'r') as fl:
            reader = csv.reader(fl)
            for row in reader:
                for elem in row:
                    self.lst.append(elem.split('\t'))
        return self.lst

    def model(self):
        final_lst = []
        for elem in self.converter()[1:len(self.converter()) - 1]:
                try:
                    if self.min_lat <= float(elem[6]) <=self.max_lat and self.min_long <= float(elem[7]) <= self.max_long:
                        final_lst.append([elem[2], elem[3], elem[6], elem[7]])
                    else:
                        continue
                except IndexError:
                    pass
        return ('\n'.join(map(str,(final_lst))))

    def __str__(self):
        return f' Аэропорты следующих городов находятся в границах указанных Вами координат: \n {self.model()}'



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Search(start_air_search):
    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(500, 800)
        Search.setStyleSheet("background-color: rgb(255, 116, 52);")
        self.centralwidget = QtWidgets.QWidget(Search)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 195, 152);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(120, 360, 260, 32))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.search.setFont(font)
        self.search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search.setObjectName("search")
        self.min_lat = QtWidgets.QLineEdit(self.centralwidget)
        self.min_lat.setGeometry(QtCore.QRect(120, 120, 260, 21))
        self.min_lat.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.min_lat.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.min_lat.setObjectName("min_lat")
        self.max_lat = QtWidgets.QLineEdit(self.centralwidget)
        self.max_lat.setGeometry(QtCore.QRect(120, 180, 260, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.max_lat.setFont(font)
        self.max_lat.setAutoFillBackground(False)
        self.max_lat.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.max_lat.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.max_lat.setObjectName("max_lat")
        self.min_lon = QtWidgets.QLineEdit(self.centralwidget)
        self.min_lon.setGeometry(QtCore.QRect(120, 240, 260, 21))
        self.min_lon.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.min_lon.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.min_lon.setObjectName("min_lon")
        self.max_lon = QtWidgets.QLineEdit(self.centralwidget)
        self.max_lon.setGeometry(QtCore.QRect(120, 300, 260, 21))
        self.max_lon.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.max_lon.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.max_lon.setObjectName("max_lon")
        self.output_info = QtWidgets.QTextEdit(self.centralwidget)
        self.output_info.setGeometry(QtCore.QRect(10, 410, 481, 371))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.output_info.setFont(font)
        self.output_info.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output_info.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 160, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 220, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 280, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        Search.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Search)
        self.statusbar.setObjectName("statusbar")
        Search.setStatusBar(self.statusbar)

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

        self.add_functions()

    def add_functions(self):
        self.search.clicked.connect(self.result)

    def result(self):
        try:
            self.output_info.setText(str(start_air_search(min_lat = float(self.min_lat.text()), max_lat = float(self.max_lat.text()), min_long = float(self.min_lon.text()), max_long = float(self.max_lon.text()))))
        except ValueError:
            pass


    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "Поиск Аэропортов v.0.0.1b"))
        self.label.setText(_translate("Search", "Выберите диапазон координат"))
        self.search.setText(_translate("Search", "Поиск"))
        self.output_info.setText(_translate("Search", " "))
        self.label_3.setText(_translate("Search", "Выберите минимальную широту (min -180)"))
        self.label_4.setText(_translate("Search", "Выберите максимальную широту(max 180)"))
        self.label_5.setText(_translate("Search", "Выберите минимальную долготу(min -180)"))
        self.label_6.setText(_translate("Search", "Выберите максимальную долготу(max 180)"))