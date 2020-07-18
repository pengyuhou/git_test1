from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("???????")
window.resize(500, 500)
window.move(400, 200)

label = QLabel(window)

label.setText('hpyhpyhpy')
label.move(425, 350)

window.show()
sys.exit(app.exec_())

