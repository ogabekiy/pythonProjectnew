from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
import sys

app = QApplication(sys.argv)


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('15 Game')
        self.setWindowIcon(QIcon('i.png'))
        self.setFixedSize(570, 800)
        self.setStyleSheet('background-color: #6a5acd;')

        self.start = QPushButton('Start', self)
        self.start.setFont(QFont('Times', 20))
        self.start.setGeometry(130, 670, 280, 100)
        self.start.setStyleSheet('background-color: blcack; color: white; border-radius:10px;')

        self.ye = 0
        self.moves = QLabel(f'Moves: {self.ye}', self)
        self.moves.setFont(QFont('Times', 20))
        self.moves.setGeometry(370, 570, 300, 100)
        self.moves.setStyleSheet('color: white;')

        self.b1 = QPushButton('1', self)
        self.b1.setFont(QFont('Times', 25))
        self.b1.setGeometry(10, 10, 130, 130)

        self.b2 = QPushButton('2', self)
        self.b2.setFont(QFont('Times', 25))
        self.b2.setGeometry(150, 10, 130, 130)

        self.b3 = QPushButton('3', self)
        self.b3.setFont(QFont('Times', 25))
        self.b3.setGeometry(290, 10, 130, 130)

        self.b4 = QPushButton('4', self)
        self.b4.setFont(QFont('Times', 25))
        self.b4.setGeometry(430, 10, 130, 130)

        self.b5 = QPushButton('5', self)
        self.b5.setFont(QFont('Times', 25))
        self.b5.setGeometry(10, 150, 130, 130)

        self.b6 = QPushButton('6', self)
        self.b6.setFont(QFont('Times', 25))
        self.b6.setGeometry(150, 150, 130, 130)

        self.b7 = QPushButton('7', self)
        self.b7.setFont(QFont('Times', 25))
        self.b7.setGeometry(290, 150, 130, 130)

        self.b8 = QPushButton('8', self)
        self.b8.setFont(QFont('Times', 25))
        self.b8.setGeometry(430, 150, 130, 130)

        self.b9 = QPushButton('9', self)
        self.b9.setFont(QFont('Times', 25))
        self.b9.setGeometry(10, 290, 130, 130)

        self.b10 = QPushButton('10', self)
        self.b10.setFont(QFont('Times', 25))
        self.b10.setGeometry(150, 290, 130, 130)

        self.b11 = QPushButton('11', self)
        self.b11.setFont(QFont('Times', 25))
        self.b11.setGeometry(290, 290, 130, 130)

        self.b12 = QPushButton('12', self)
        self.b12.setFont(QFont('Times', 25))
        self.b12.setGeometry(430, 290, 130, 130)

        self.b13 = QPushButton('13', self)
        self.b13.setFont(QFont('Times', 25))
        self.b13.setGeometry(10, 430, 130, 130)

        self.b14 = QPushButton('14', self)
        self.b14.setFont(QFont('Times', 25))
        self.b14.setGeometry(150, 430, 130, 130)

        self.b15 = QPushButton('15', self)
        self.b15.setFont(QFont('Times', 25))
        self.b15.setGeometry(290, 430, 130, 130)

        self.b16 = QPushButton('', self)
        self.b16.setFont(QFont('Times', 25))
        self.b16.setGeometry(430, 430, 130, 130)

        self.b1.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b2.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b3.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b4.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b5.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b6.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b7.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b8.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b9.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b10.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b11.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b12.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b13.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b14.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b15.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b16.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        self.b1.clicked.connect(self.bosildi)
        self.b2.clicked.connect(self.bosildi)
        self.b3.clicked.connect(self.bosildi)
        self.b4.clicked.connect(self.bosildi)
        self.b5.clicked.connect(self.bosildi)
        self.b6.clicked.connect(self.bosildi)
        self.b7.clicked.connect(self.bosildi)
        self.b8.clicked.connect(self.bosildi)
        self.b9.clicked.connect(self.bosildi)
        self.b10.clicked.connect(self.bosildi)
        self.b11.clicked.connect(self.bosildi)
        self.b12.clicked.connect(self.bosildi)
        self.b13.clicked.connect(self.bosildi)
        self.b14.clicked.connect(self.bosildi)
        self.b15.clicked.connect(self.bosildi)
        self.b16.clicked.connect(self.bosildi)

        self.start.clicked.connect(self.chayib_ber)

        self.b1.clicked.connect(self.bos1)
        self.b2.clicked.connect(self.bos2)
        self.b3.clicked.connect(self.bos3)
        self.b4.clicked.connect(self.bos4)
        self.b5.clicked.connect(self.bos5)
        self.b6.clicked.connect(self.bos6)
        self.b7.clicked.connect(self.bos7)
        self.b8.clicked.connect(self.bos8)
        self.b9.clicked.connect(self.bos9)
        self.b10.clicked.connect(self.bos10)
        self.b11.clicked.connect(self.bos11)
        self.b12.clicked.connect(self.bos12)
        self.b13.clicked.connect(self.bos13)
        self.b14.clicked.connect(self.bos14)
        self.b15.clicked.connect(self.bos15)
        self.b16.clicked.connect(self.bos16)

        # self.b2.clicked.connect(self.joyini_topdi)
        # self.b3.clicked.connect(self.joyini_topdi)
        # self.b4.clicked.connect(self.joyini_topdi)
        # self.b5.clicked.connect(self.joyini_topdi)
        # self.b6.clicked.connect(self.joyini_topdi)
        # self.b7.clicked.connect(self.joyini_topdi)
        # self.b8.clicked.connect(self.joyini_topdi)
        # self.b9.clicked.connect(self.joyini_topdi)
        # self.b10.clicked.connect(self.joyini_topdi)
        # self.b11.clicked.connect(self.joyini_topdi)
        # self.b12.clicked.connect(self.joyini_topdi)
        # self.b13.clicked.connect(self.joyini_topdi)
        # self.b14.clicked.connect(self.joyini_topdi)
        # self.b15.clicked.connect(self.joyini_topdi)
        # self.b16.clicked.connect(self.joyini_topdi)

        self.ran = 0
        self.lis = []

    def bosildi(self):
        # self.ye +=1
        # self.moves.setText(f'Moves: {self.ye}')

        but1 = self.b1.text()
        but2 = self.b2.text()
        but3 = self.b3.text()
        but4 = self.b4.text()
        but5 = self.b5.text()
        but6 = self.b6.text()
        but7 = self.b7.text()
        but8 = self.b8.text()
        but9 = self.b9.text()
        but10 = self.b10.text()
        but11 = self.b11.text()
        but12 = self.b12.text()
        but13 = self.b13.text()
        but14 = self.b14.text()
        but15 = self.b15.text()
        but16 = self.b16.text()

        if but1 == '1':
            self.b1.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b1.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        if but2 == '2':
            self.b2.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b2.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but3 == '3':
            self.b3.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b3.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but4 == '4':
            self.b4.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b4.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but5 == '5':
            self.b5.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b5.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but6 == '6':
            self.b6.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b6.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but7 == '7':
            self.b7.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b7.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but8 == '8':
            self.b8.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b8.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but9 == '9':
            self.b9.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b9.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but10 == '10':
            self.b10.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b10.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but11 == '11':
            self.b11.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b11.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but12 == '12':
            self.b12.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b12.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but13 == '13':
            self.b13.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b13.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but14 == '14':
            self.b14.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b14.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but15 == '15':
            self.b15.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b15.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

        if but16 == '':
            self.b16.setStyleSheet('background-color: #ffadb9; color: white; border-radius: 5px; border: black')
        else:
            self.b16.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

    def chayib_ber(self):
        import random
        n = list(range(0, 16))
        random.shuffle(n)
        self.lis = n
        self.ye = 0
        self.moves.setText(f'Moves: {self.ye}')

        for i in range(16):
            if n[i] == 0:
                n[i] = ''
                self.ran = i
                break

        self.b1.setText(str(n[0]))
        self.b2.setText(str(n[1]))
        self.b3.setText(str(n[2]))
        self.b4.setText(str(n[3]))
        self.b5.setText(str(n[4]))
        self.b6.setText(str(n[5]))
        self.b7.setText(str(n[6]))
        self.b8.setText(str(n[7]))
        self.b9.setText(str(n[8]))
        self.b10.setText(str(n[9]))
        self.b11.setText(str(n[10]))
        self.b12.setText(str(n[11]))
        self.b13.setText(str(n[12]))
        self.b14.setText(str(n[13]))
        self.b15.setText(str(n[14]))
        self.b16.setText(str(n[15]))

        self.b1.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b2.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b3.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b4.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b5.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b6.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b7.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b8.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b9.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b10.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b11.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b12.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b13.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b14.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b15.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')
        self.b16.setStyleSheet('background-color: #add8ef; color: white; border-radius: 5px; border: black')

    def bos1(self):
        but = self.b1.text()
        but2 = self.b2.text()
        but5 = self.b5.text()
        if but2 == '':
            self.b1.setText('')
            self.b2.setText(str(but))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but5 == '':
            self.b1.setText('')
            self.b5.setText(str(but))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos2(self):
        but2 = self.b2.text()
        but3 = self.b3.text()
        but6 = self.b6.text()
        but1 = self.b1.text()
        if but1 == '':
            self.b2.setText('')
            self.b1.setText(str(but2))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but3 == '':
            self.b2.setText('')
            self.b3.setText(str(but2))
        if but6 == '':
            self.b2.setText('')
            self.b6.setText(str(but2))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos3(self):
        but3 = self.b3.text()
        but2 = self.b2.text()
        but4 = self.b4.text()
        but7 = self.b7.text()
        if but2 == '':
            self.b3.setText('')
            self.b2.setText(str(but3))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but4 == '':
            self.b3.setText('')
            self.b4.setText(str(but3))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but7 == '':
            self.b3.setText('')
            self.b7.setText(str(but3))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos4(self):
        but4 = self.b4.text()
        but3 = self.b3.text()
        but8 = self.b8.text()
        if but3 == '':
            self.b4.setText('')
            self.b3.setText(str(but4))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but8 == '':
            self.b4.setText('')
            self.b8.setText(str(but4))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos5(self):
        but5 = self.b5.text()
        but1 = self.b1.text()
        but6 = self.b6.text()
        but9 = self.b9.text()
        if but1 == '':
            self.b5.setText('')
            self.b1.setText(str(but5))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but6 == '':
            self.b5.setText('')
            self.b6.setText(str(but5))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but9 == '':
            self.b5.setText('')
            self.b9.setText(str(but5))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos6(self):
        but6 = self.b6.text()
        but2 = self.b2.text()
        but5 = self.b5.text()
        but7 = self.b7.text()
        but10 = self.b10.text()
        if but2 == '':
            self.b6.setText('')
            self.b2.setText(str(but6))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but5 == '':
            self.b6.setText('')
            self.b5.setText(str(but6))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but7 == '':
            self.b6.setText('')
            self.b7.setText(str(but6))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but10 == '':
            self.b6.setText('')
            self.b10.setText(str(but6))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos7(self):
        but7 = self.b7.text()
        but3 = self.b3.text()
        but6 = self.b6.text()
        but11 = self.b11.text()
        but8 = self.b8.text()
        if but3 == '':
            self.b7.setText('')
            self.b3.setText(str(but7))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but6 == '':
            self.b7.setText('')
            self.b6.setText(str(but7))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but11 == '':
            self.b7.setText('')
            self.b11.setText(str(but7))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but8 == '':
            self.b7.setText('')
            self.b8.setText(str(but7))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos8(self):
        but8 = self.b8.text()
        but4 = self.b4.text()
        but7 = self.b7.text()
        but12 = self.b12.text()
        if but4 == '':
            self.b8.setText('')
            self.b4.setText(str(but8))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but7 == '':
            self.b8.setText('')
            self.b7.setText(str(but8))
        if but12 == '':
            self.b8.setText('')
            self.b12.setText(str(but8))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos9(self):
        but9 = self.b9.text()
        but5 = self.b5.text()
        but10 = self.b10.text()
        but13 = self.b13.text()
        if but5 == '':
            self.b9.setText('')
            self.b5.setText(str(but9))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but10 == '':
            self.b9.setText('')
            self.b10.setText(str(but9))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but13 == '':
            self.b9.setText('')
            self.b13.setText(str(but9))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos10(self):
        but10 = self.b10.text()
        but6 = self.b6.text()
        but9 = self.b9.text()
        but11 = self.b11.text()
        but14 = self.b14.text()
        if but6 == '':
            self.b10.setText('')
            self.b6.setText(str(but10))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but9 == '':
            self.b10.setText('')
            self.b9.setText(str(but10))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but11 == '':
            self.b10.setText('')
            self.b11.setText(str(but10))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but14 == '':
            self.b10.setText('')
            self.b14.setText(str(but10))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos11(self):
        but11 = self.b11.text()
        but7 = self.b7.text()
        but10 = self.b10.text()
        but12 = self.b12.text()
        but15 = self.b15.text()
        if but7 == '':
            self.b11.setText('')
            self.b7.setText(str(but11))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but10 == '':
            self.b11.setText('')
            self.b10.setText(str(but11))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but12 == '':
            self.b11.setText('')
            self.b12.setText(str(but11))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but15 == '':
            self.b11.setText('')
            self.b15.setText(str(but11))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos12(self):
        but12 = self.b12.text()
        but8 = self.b8.text()
        but11 = self.b11.text()
        but16 = self.b16.text()
        if but8 == '':
            self.b12.setText('')
            self.b8.setText(str(but12))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but11 == '':
            self.b12.setText('')
            self.b11.setText(str(but12))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but16 == '':
            self.b12.setText('')
            self.b16.setText(str(but12))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos13(self):
        but13 = self.b13.text()
        but9 = self.b9.text()
        but14 = self.b14.text()
        if but9 == '':
            self.b13.setText('')
            self.b9.setText(str(but13))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but14 == '':
            self.b13.setText('')
            self.b14.setText(str(but13))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos14(self):
        but14 = self.b14.text()
        but13 = self.b13.text()
        but10 = self.b10.text()
        but15 = self.b15.text()
        if but13 == '':
            self.b14.setText('')
            self.b13.setText(str(but13))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but10 == '':
            self.b14.setText('')
            self.b10.setText(str(but14))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but15 == '':
            self.b14.setText('')
            self.b15.setText(str(but14))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos15(self):
        but15 = self.b15.text()
        but11 = self.b11.text()
        but14 = self.b14.text()
        but16 = self.b16.text()
        if but11 == '':
            self.b15.setText('')
            self.b11.setText(str(but15))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but14 == '':
            self.b15.setText('')
            self.b14.setText(str(but15))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but16 == '':
            self.b15.setText('')
            self.b16.setText(str(but15))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')

    def bos16(self):
        but16 = self.b16.text()
        but12 = self.b12.text()
        but15 = self.b15.text()
        if but12 == '':
            self.b16.setText('')
            self.b12.setText(str(but16))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')
        if but15 == '':
            self.b16.setText('')
            self.b15.setText(str(but16))
            self.ye += 1
        self.moves.setText(f'Moves: {self.ye}')


oyna = Oyna()
oyna.show()
app.exec_()