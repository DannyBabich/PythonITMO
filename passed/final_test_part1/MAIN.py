from PyQt5 import QtWidgets
import UI_AIR

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AirportSearch = QtWidgets.QStackedWidget()
    ui = UI_AIR.Ui_AirportSearch()
    ui.setupUi(AirportSearch)
    AirportSearch.show()
    sys.exit(app.exec_())


