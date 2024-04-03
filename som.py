from PyQt5.QtWidgets import QApplication,QMainWindow,QVBoxLayout,QLabel,QWidget,QPushButton, QLineEdit


flex = QApplication([])



class try2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BASIC")
        self.setFixedSize(500,500)
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
        a = str(txt)
        s = ""
        for i in a:
            if i.isdigit():
                s+=i
            else:
                s+=" "
        l = s.split()
        ll=list()
        for i in l:
            ll.append(int(i))
        ll.sort()
        lk = ll[::-1]
        res=""
        for i in lk:
            res+=str(i)
            res+=" "

        self.mana.setText(f"{res}")

oyna = try2()
oyna.show()
flex.exec()

