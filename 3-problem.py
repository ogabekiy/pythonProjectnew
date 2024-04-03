from PyQt5.QtWidgets import QApplication,QMainWindow,QVBoxLayout,QLabel,QWidget,QPushButton, QLineEdit


flex = QApplication([])



class try2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BASIC")
        self.setFixedSize(400,300)
        self.sonkirit = QLineEdit()
        self.bttn = QPushButton("press")
        self.mana = QLabel("result here...")

        self.q_widget = QWidget()
        self.asosiy = QVBoxLayout(self.q_widget)

        self.asosiy.addWidget(self.sonkirit)
        self.asosiy.addWidget(self.bttn)
        self.asosiy.addWidget(self.mana)

        self.setCentralWidget(self.q_widget)
        self.bttn.clicked.connect(self.natural)
    def natural(self):
        txt = self.sonkirit.text()
        a = txt
        l=list()
        for i in a:
            if i.isdigit():
                s = ""
                for j in range(i,len(a)):
                    if i[j].isdigit():
                        s+=i[j]
                    else:
                        break
                    break
                l.append(int(s))

        # self.mana.setText(f"{sorted(l)}")

oyna = try2()
oyna.show()
flex.exec()



