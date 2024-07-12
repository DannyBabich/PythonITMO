import start_air_search


if __name__ == "__main__":
    import sys
    app = start_air_search.QtWidgets.QApplication(sys.argv)
    Search = start_air_search.QtWidgets.QMainWindow()
    ui = start_air_search.Ui_Search(0,0,0,0)
    ui.setupUi(Search)
    Search.show()
    sys.exit(app.exec_())


