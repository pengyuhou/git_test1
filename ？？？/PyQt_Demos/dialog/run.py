import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
import test

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
