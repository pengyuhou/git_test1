`from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hpynb')
        self.resize(500, 400)
        self.setup_ui()
    def setup_ui(self):
        $code$


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.setup_ui()
    window.show()
    sys.exit(app.exec_())

`