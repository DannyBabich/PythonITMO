from PyQt5 import QtWidgets
import UI

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search = QtWidgets.QMainWindow()
    ui = UI.Ui_Search()
    ui.setupUi(Search)
    Search.show()
    sys.exit(app.exec_())


