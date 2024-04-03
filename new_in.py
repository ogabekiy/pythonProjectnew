from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout

flex = QApplication([])


class try2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Miles to Kilometres")
        self.setFixedSize(500,200)
        self.a = QLabel("Dinstance in Miles: ")
        self.b = QLabel("Distance in Kilometres: ")
        self.sonkirit = QLineEdit()
        self.bttn = QPushButton("Convert")
        self.mana = QLineEdit()


        self.line1_w = QWidget()
        self.line1_lay = QHBoxLayout()
        self.line1_w.setLayout(self.line1_lay)

        self.line1_lay.addWidget(self.a)
        self.line1_lay.addWidget(self.sonkirit)

        self.line2_w = QWidget()
        self.line2_lay = QHBoxLayout()
        self.line2_w.setLayout(self.line2_lay)

        self.line2_lay.addWidget(self.b)
        self.line2_lay.addWidget(self.mana)


        self.q_widget = QWidget()
        self.asosiy = QVBoxLayout(self.q_widget)

        self.asosiy.addWidget(self.line1_w)
        self.asosiy.addWidget(self.bttn)
        self.asosiy.addWidget(self.line2_w)

        self.setCentralWidget(self.q_widget)
        self.bttn.clicked.connect(self.natural)
    def natural(self):
        txt = self.sonkirit.text()
        a = int(txt)
        res = a * 1.60934
        self.mana.setText(f"{res}")

oyna = try2()
oyna.show()
flex.exec()

