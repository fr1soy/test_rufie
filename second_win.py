from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from final_win import *



class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connnects()
        self.show()

    def next_click(self):
        pass

    def connects(self):
        pass

    def set_appeat(self):
        pass

    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults)
        self.btn_test1 = QLabel(txt_starttest1)
        self.btn_test2 = QLabel(txt_starttest2)
        self.btn_test3 = QLabel(txt_starttest3)

        self.text_name = Qlabel(txt_name)
        self.text_age = Qlabel(txt_age)
        self.text_test1 = Qlabel(txt_test1)
        self.text_test2 = Qlabel(txt_test2)
        self.text_test3 = Qlabel(txt_test3)

        self.text_timer = Qlabel(txt_timer)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintname)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QVBoxLayout()

        self.r_line.addWidget(self.text_timer, alignment= Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.line_name, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.text_age, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.line_age, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.text_test1, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.btn_test1, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.text_test2, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.btn_test2, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.text_test3, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.btn_test3, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.line_test2, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.line_test3, alignment= Qt.Alignleft)
        self.l_line.addWidget(self.btn_next, alignment= Qt.Alignleft)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
       

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.line = QVBoxLayout()# напиши здесь код для второго экрана приложения
