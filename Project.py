from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox


def show_win():
    win = QMessageBox()
    win.setWindowTitle('Правильно!')
    win.setText('ВЕРНО!')
    win.exec_()


def loose():
    loose = QMessageBox()
    loose.setWindowTitle('НЕПРАВИЛЬНО!')
    loose.setText('Вы проиграли(')
    loose.exec_()


app = QApplication([])
main_win = QWidget()
main_win.resize(700, 500)
main_win.setWindowTitle('Викторина')
answer = QLabel('Когда был создан язык Python?:')
button1 = QRadioButton('1989')
button2 = QRadioButton('1891')
button3 = QRadioButton('1911')
button4 = QRadioButton('1999')
button1.clicked.connect(show_win)
button2.clicked.connect(loose)
button3.clicked.connect(loose)
button4.clicked.connect(loose)
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line1.addWidget(answer, alignment=Qt.AlignCenter)
h_line2.addWidget(button1, alignment=Qt.AlignCenter)
h_line2.addWidget(button3, alignment=Qt.AlignCenter)
h_line3.addWidget(button2, alignment=Qt.AlignCenter)
h_line3.addWidget(button4, alignment=Qt.AlignCenter)
v_line = QVBoxLayout()
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)
main_win.setLayout(v_line)

main_win.show()
app.exec_()
