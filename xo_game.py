from PyQt5.QtWidgets import QMainWindow, QMessageBox, QGridLayout, QPushButton, QWidget, QApplication

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lay = QGridLayout()
        self.main_wid = QWidget()
        self.main_wid.setLayout(self.lay)
        self.l = []
        self.reset_btn = QPushButton("RESET!")
        self.reset_btn.setFixedHeight(80)
        self.reset_btn.clicked.connect(self.button_reset)
        self.yutish_kombinatsiyalari = [[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9],
                                        [1, 5, 9],
                                        [3, 5, 7],
                                        [1, 4, 7],
                                        [2, 5, 8],
                                        [3, 6, 9]]
        self.xlar = []
        self.nollar = []

        self.x = True
        c = 0
        for i in range(9):
            self.l.append(QPushButton(""))
            self.l[i].setFixedSize(250, 250)
            self.l[i].setStyleSheet("font-size:75px")
            self.l[i].clicked.connect(self.bosildi)
            self.l[i].setProperty("belgi", f"{i + 1}")
            self.lay.addWidget(self.l[i], c, i % 3)
            if i % 3 == 2:
                c += 1
        self.lay.addWidget(self.reset_btn, 3, 1)
        self.setCentralWidget(self.main_wid)

    def bosildi(self):
        print()
        if self.x:
            self.sender().setText("X")
            self.xlar.append(int(self.sender().property("belgi")))
        else:
            self.sender().setText("0")
            self.nollar.append(int(self.sender().property("belgi")))
        print(self.xlar)
        print(self.nollar)
        self.x = not self.x
        self.sender().setEnabled(False)
        self.check_win()

    def check_win(self):
        for i in self.yutish_kombinatsiyalari:
            if set(i).issubset(self.xlar):
                QMessageBox.information(self,"xwin", "xlar g'olib!!!")
                for j in self.l:
                    j.setEnabled(False)
                self.button_boya(i)
            elif set(i).issubset(self.nollar):
                QMessageBox.information(self, "0win", "nollar g'olib!!!", )
                for j in self.l:
                    j.setEnabled(False)
                self.button_boya(i)


    def button_boya(self, indices):
        for i in indices:
            self.l[i-1].setStyleSheet("background-color: green; font-size:75px; color: white")


    def button_reset(self):
        for j in self.l:
            j.setText("")
            j.setStyleSheet("background-color: grey; font-size:75px")
            j.setEnabled(True)
        self.xlar.clear()
        self.nollar.clear()


a = MainWindow()
a.show()
app.exec()
