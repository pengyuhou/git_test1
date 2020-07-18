from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hpynb')
        self.resize(500, 400)
        self.setup_ui()

    def setup_ui(self):
        self.test1()

    def test1(self):
        # ********  测试API    *************
        # obj = QObject()
        # obj.setObjectName('a')
        # obj.setProperty('name', 'hpy')
        # obj.setProperty('age', 20)
        # print(obj.property('name'))
        # print(obj.property('age'))
        # **********************

        label = QLabel(self)
        label.setObjectName('notice')
        label.setProperty('notice_level', 'normal')
        label.setText('hpynb')



        label2 = QLabel(self)
        label2.setObjectName('notice')
        label2.setProperty('notice_level', 'waring')

        label2.setText('yes')
        label2.move(50, 100)

        btn1 = QPushButton(self)
        btn1.setText('click')
        btn1.move(50, 50)

        # qss
        with open('QLabel.qss', 'r') as fp:
            app.setStyleSheet(fp.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
