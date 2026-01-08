import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        buttonheight=120

        self.setWindowTitle("Stereo Vision Capstone")

        layout=QVBoxLayout()
        layout.addWidget(QPushButton("1"))
        layout.addWidget(QPushButton("2"))
        layout.addWidget(QPushButton("3"))
        layout.addWidget(QPushButton("4"))


        button1 = QPushButton("1")
        button1.clicked.connect(self.button1click)
        button1.setFixedHeight(buttonheight)

        button2 = QPushButton("2")
        button2.clicked.connect(self.button2click)
        button2.setFixedHeight(buttonheight)

        button3 = QPushButton("3")
        button3.clicked.connect(self.button3click)
        button3.setFixedHeight(buttonheight)

        button4 = QPushButton("4")
        button4.clicked.connect(self.button4click)
        button4.setFixedHeight(buttonheight)

        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def button1click(self):
        #first button code
        print("hi1")

    def button2click(self):
        #second button code
        print("hi2")

    def button3click(self):
        #first button code
        print("hi3")

    def button4click(self):
        #first button code
        print("hi4")


    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()