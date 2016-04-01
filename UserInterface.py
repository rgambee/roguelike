import sys
from PyQt5.QtWidgets import QApplication, QWidget
print 'import'
app = QApplication(sys.argv)
print 'app'
w = QWidget()
w.resize(250, 150)
w.move(300, 300)
w.set_title('Window Title')
w.show()

app.exec_()