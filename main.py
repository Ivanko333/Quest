from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint


def show_winner():
    ramdomazir = str(randint(0, 10000))
    button.setText(ramdomazir)


app = QApplication([])
main_win = QWidget()
main_win.resize(200, 200)
main_win.setWindowTitle('Рамдомайзер')
winner = QLabel('ЧИСЛО:')
button = QPushButton('СГЕНЕРИРОВАТЬ')
v_line = QVBoxLayout()
v_line.addWidget(winner, alignment=Qt.AlignCenter)
v_line.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(v_line)
button.clicked.connect(show_winner)
main_win.show()
app.exec_()
